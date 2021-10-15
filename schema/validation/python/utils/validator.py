'''
Created on 2021/07/01

@author: laurentmichel
'''

import re, xmlschema


class Validator:

    def __init__(self, xsd_path):
        self.xmlschema = xmlschema.XMLSchema11(xsd_path)

    def validate_file(self, xml_path: str, verbose=False, expected_fail_msg=None) -> bool:
        if verbose is True:
            try :
                self.xmlschema.validate(xml_path)
                return True
            except Exception as e:
                if expected_fail_msg is not None:
                    if expected_fail_msg in str(e):
                        # Expected error
                        return True
                    # The error message can differ from the expected one by some string layout that can 
                    # depends on the XSD processor e.g Xpath elements quoted or not
                    elif (expected_fail_msg is not None 
                          and expected_fail_msg.replace("'", "").replace(" ", "").replace('"', '') 
                          in str(e).replace("'", "").replace(" ", "").replace('"', '')):
                        return True
                    # When an error occurs on the lack of a required attribute, the message may change 
                    # From a validator to another.
                    # Here is a little hack to work this around.
                    elif expected_fail_msg.startswith("missing required attribute") is True:
                        e_msg = str(e)
                        att_name = re.search(r'^missing required attribute \'(.*)\'$', expected_fail_msg).group(1)
                        p = re.compile(r'failed validating .* with XsdAttributeGroup(.*' + att_name +'.*)')
                        if p.match(e_msg) is None:
                            print("Failure message: \n{}".format(e))
                            print("Expected reason: {}".format(expected_fail_msg))
    
                            return False
                        return True
                    else:
                        print("Failure message: \n{}".format(e))

                        return False
                # Not Expected errror
                print("Failure reason: {}".format(e))
                return False
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
