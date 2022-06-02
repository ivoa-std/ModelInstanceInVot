'''
Created on 9 Apr 2022

@author: laurentmichel
'''
import xmlschema, lxml

schema = xmlschema.XMLSchema11("essai.xsd")

print(schema.is_valid("essai.xml"))

schema = xmlschema.XMLSchema11("../../../xsd/mivot-v1.0.xsd")
print(schema.validate("../../snippets/test_9_ok.xml"))
print(schema.validate("../../snippets/test_9_ko_9.2.xml"))
