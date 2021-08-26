'''
Created on 2021/07/01

@author: laurentmichel
'''
import os
import xmlschema
from utils.validator import Validator
from utils.file_utils import FileUtils
from utils import logger

class TestVOTableRunner:
    validator = Validator("http://www.ivoa.net/xml/VOTable/v1.3")
        
    vodml_validator = Validator(os.path.join(FileUtils.get_schemadir()
                                   , "merged-syntax.xsd"))
    vodml_validator = Validator("https://raw.githubusercontent.com/ivoa-std/ModelInstanceInVot/master/schema/xsd/merged-syntax.xsd")

    @staticmethod
    def testOK(mapping_sample, case_prefix):
        files = os.listdir(mapping_sample)
        ok_prefix = case_prefix + "_ok"

        for sample_file in files:
            if sample_file.startswith(ok_prefix) is True:
                file_path = os.path.join(mapping_sample, sample_file)
                if TestVOTableRunner.validator.validate_file(file_path, verbose=False) is False:
                    TestVOTableRunner.validator.validate_file(file_path, verbose=True)
                    logger.error(sample_file + " is not valid, it should be")
                    return  False
                logger.info(sample_file + " is valid: fine")
                TestVOTableRunner.vodml_validator.validate_file(file_path, verbose=False)
                import xml.etree.ElementTree as etree
                ns = {'dm': 'https://raw.githubusercontent.com/ivoa-std/ModelInstanceInVot/master/schema/xsd/merged-syntax.xsd'}
                tree = etree.parse(file_path)
                root = tree.getroot()
                for actor in root.findall('{http://www.ivoa.net/xml/VOTable/v1.3}RESOURCE'):
                    print("=====")
                    for vodml in actor.findall('dm:VODML', ns):
                        print(etree.tostring(vodml).decode())
                        TestVOTableRunner.vodml_validator.validate_string(etree.tostring(vodml).decode())
                xs = xmlschema.XMLSchema11('https://raw.githubusercontent.com/ivoa-std/ModelInstanceInVot/master/schema/xsd/merged-syntax.xsd')
                #print(xs.is_valid(tree))
                from pprint import pprint
                #pprint(xs.to_dict(tree, process_namespaces=False))
        return True
    
    @staticmethod
    def testKO(mapping_sample, case_prefix):
 
        ko_prefix = case_prefix + "_ko"
        files = os.listdir(mapping_sample)

        for sample_file in files:
            if sample_file.startswith(ko_prefix) is True:
                file_path = os.path.join(mapping_sample, sample_file)
                if TestVOTableRunner.validator.validate_file(file_path , verbose=False) is True:
                    logger.error(sample_file)
                    return False
                logger.info(sample_file + " is not valid: fine")
        return True
