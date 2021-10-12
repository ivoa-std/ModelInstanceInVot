'''
Created on 2021/07/01

@author: laurentmichel
'''
import os
import pytest
from utils.validator import Validator
from utils.file_utils import FileUtils
from utils import logger

class TestRunner:
    schemafile = os.path.join(FileUtils.get_schemadir(), "merged-syntax.xsd")
    validator = Validator(schemafile)
    
    @staticmethod
    def regarde_si_OK(mapping_sample, case_prefix):
        # Sorry for the French naming, so that I'm sure pytest won't take as a fixture
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
    def regarde_si_KO(mapping_sample, case_prefix, expected=None):
 
        ko_prefix = case_prefix + "_ko"
        files = os.listdir(mapping_sample)

        for sample_file in files:
            if sample_file.startswith(ko_prefix) is True:
                file_path = os.path.join(mapping_sample, sample_file)
                if TestRunner.validator.validate_file(file_path , verbose=False) is True:
                    # file is valid.. that's a problem.
                    logger.error(sample_file + " validates: problem")
                    return False
                else:
                    # file is invalid.. check why
                    if expected is not None:
                        test_case = sample_file.split(ko_prefix+"_")[1].split('.xml')[0]
                        errmsg = expected.get( test_case, None )
                        if errmsg is not None:
                            # we have an expected fail reason.. screen validation with this info.
                            if TestRunner.validator.validate_file(file_path, verbose=True, expected_fail_msg=errmsg ) is True:
                                logger.info(sample_file + " is not valid.. for expected reason: fine")
                                continue
                            else:
                                # file is not valid, but for the wrong reason.. problem.
                                logger.error(sample_file + " is not valid.. for wrong reason: problem")
                                return False

                    # no expected information given, we just care that it is not valid.
                    logger.info(sample_file + " is not valid: fine")
        return True
