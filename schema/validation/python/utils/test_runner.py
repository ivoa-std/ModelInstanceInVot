'''
Created on 2021/07/01

@author: laurentmichel
'''
import os
from utils.validator import Validator
from utils.file_utils import FileUtils
from utils import logger

class TestRunner:
    validator = Validator(os.path.join(FileUtils.get_schemadir()
                                   , "merged-syntax.xsd"))
    
    @staticmethod
    def testOK(mapping_sample, case_prefix):
        files = os.listdir(mapping_sample)
        ok_prefix = case_prefix + "_ok"

        for sample_file in files:
            if sample_file.startswith(ok_prefix) is True:
                file_path = os.path.join(mapping_sample, sample_file)
                if TestRunner.validator.validate_file(file_path, verbose=False) is False:
                    TestRunner.validator.validate_file(file_path, verbose=True)
                    logger.error(sample_file + " is not valid, it should be")
                    return  False
                logger.info(sample_file + " is valid: fine")
        return True
    
    @staticmethod
    def testKO(mapping_sample, case_prefix):
 
        ko_prefix = case_prefix + "_ko"
        files = os.listdir(mapping_sample)

        for sample_file in files:
            if sample_file.startswith(ko_prefix) is True:
                file_path = os.path.join(mapping_sample, sample_file)
                if TestRunner.validator.validate_file(file_path , verbose=False) is True:
                    logger.error(sample_file)
                    return False
                logger.info(sample_file + " is not valid: fine")
        return True
