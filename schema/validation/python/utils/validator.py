'''
Created on 2021/07/01

@author: laurentmichel
'''

import re, xmlschema
from utils import logger


class Validator:

    def __init__(self, xsd_path, namespace=None):
        logger.info("Using %s", xsd_path)
        if namespace is not None:
            self.xmlschema = xmlschema.XMLSchema11(xsd_path)    
        else:
            self.xmlschema = xmlschema.XMLSchema11(xsd_path)

    def validate_file(self, xml_path: str, verbose=False, expected_fail_msg=None) -> bool:
        if verbose is True:
            try :
                self.xmlschema.validate(xml_path)
                return True
            except Exception as e:
                #print(e)
                return self._errorMatchExpectedMessage(e, expected_fail_msg)
        else :
            return self.xmlschema.is_valid(xml_path)
        
    def validate_string(self, xml_string: str, verbose=False) -> bool:
        if verbose is True:
            try :
                self.xmlschema.validate(xml_string)
                return True
            except Exception as e:
                print(e)
                return False
        else :
            return self.xmlschema.is_valid(xml_string)
        
    def _errorMatchExpectedMessage(self, error, expected_fail_msg):
        if expected_fail_msg is None:
            logger.info("no expected fail message")
            return True
        error_txt = str(error)
        
        if expected_fail_msg in error_txt:
            # Expected error
            logger.info("Validation error as expected (%s)", expected_fail_msg)
            return True

        if (expected_fail_msg.replace("'", "").replace(" ", "").replace('"', '') 
            in error_txt.replace("'", "").replace(" ", "").replace('"', '')):
            logger.info("Validation error looks like expected (%s)", expected_fail_msg)
            return True
        
        if expected_fail_msg.startswith("missing required attribute") is True:
            att_name = re.search(r'^missing required attribute \'(.*)\'$', expected_fail_msg).group(1)
            p = re.compile(r'failed validating .* with XsdAttributeGroup(.*' + att_name +'.*)')
            if p.match(error_txt) is None:
                logger.error("Failure message: %s", error)
                logger.error("Expected reason: %s", expected_fail_msg)
                return False
            logger.info("Validation error matches expected message (%s)", expected_fail_msg)
            return True

        logger.error("Failure message: %s", error)
        logger.error("Expected reason: %s", expected_fail_msg)
        return False
