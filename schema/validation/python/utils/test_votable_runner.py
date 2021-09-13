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
    @staticmethod
    def testOK(mapping_sample, case_prefix):
        files = os.listdir(mapping_sample)
        ok_prefix = case_prefix + "_ok"

        for sample_file in files:
            if sample_file.startswith(ok_prefix) is True:
                file_path = os.path.join(mapping_sample, sample_file)
                logger.info("Validate {} against VOTable/v1.3".format(sample_file))
                if TestVOTableRunner.validator.validate_file(file_path, verbose=False) is False:
                    TestVOTableRunner.validator.validate_file(file_path, verbose=True)
                    logger.error(sample_file + " is not valid, it should be")
                    return  False
                logger.info("passed")
                logger.info("Validate {} against merged-syntax.xsd".format(sample_file))
                if TestVOTableRunner.vodml_validator.validate_file(file_path, verbose=False) is False:
                    TestVOTableRunner.vodml_validator.validate_file(file_path, verbose=True)
                    logger.error(sample_file + " is not valid, it should be")
                    return  False                
                logger.info("passed")
                logger.info(sample_file + " is valid: fine")
        return True
    
    @staticmethod
    def testKO(mapping_sample, case_prefix):
 
        ko_prefix = case_prefix + "_ko"
        files = os.listdir(mapping_sample)

        for sample_file in files:
            if sample_file.startswith(ko_prefix) is True:
                file_path = os.path.join(mapping_sample, sample_file)
                logger.info("Validate {} against VOTable/v1.3".format(sample_file))
                passed = 0
                if TestVOTableRunner.validator.validate_file(file_path , verbose=False) is True:
                    logger.info("passed")
                    passed += 1
                else:
                    logger.info("failed")
                    
                logger.info("Validate {} against merged-syntax.xsd".format(sample_file))
                if TestVOTableRunner.vodml_validator.validate_file(file_path , verbose=False) is True:
                    logger.info("passed")
                    passed += 1
               
                if passed == 2:
                    logger.info("Both validation passed; at least one shouldn't ")
                    return False
                else:
                    logger.info("failed")

                logger.info(sample_file + " is not valid: fine")
                
                
        return True
