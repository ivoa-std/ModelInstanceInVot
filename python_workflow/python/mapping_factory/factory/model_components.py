from mapping_factory import  logger
from mapping_factory.factory.model_constraints import *

class VodmlRootType:
    def __init__(self, vodml_type, superclass, attributes, vodml_constraints, abstract=False, ref=""):
        self.vodml_type = vodml_type
        self.superclass = superclass
        self.attributes = attributes #role VodmlRootType
        self.abstract = abstract
        self.ref = ref
        self.vodml_constraints = vodml_constraints

class VodmlObjectType(VodmlRootType):
        
    def __str__(self):
        retour = ""
        if self.abstract:
            retour += "Abstract "
        retour +=  "OBJECT " 
        if self.superclass != '':
            retour += "(extends " + self.superclass + ") "
        retour += self.vodml_type + " " + self.vodmlid +"\nATTRIBUTES\n"
        for attribute in self.attributes.values():
            retour += " - " + attribute.__str__()
        #retour += "CONSTRAINTS " + self.vodml_constraints.__repr__()
        return retour
    
    def __repr__(self):
        return self.__str__()
    
                     
class VodmlDataType(VodmlRootType):   
    def __str__(self):
        return self.__repr__()
    def __repr__(self):
        retour = ""
        if self.abstract:
            retour += "Abstract "
        retour +=  "DATATYPE " + self.vodml_type + " ref" + self.ref 
        retour += "\n    ATTRIBUTES " + self.attributes.__repr__()
        #retour += "\n    " + self.vodml_constraints.__repr__()
        return retour
            
class VodmlAttribute:    
    def __init__(self, vodmlid, vodml_element, is_reference, array_size=1):
        if isinstance(vodml_element, str):
            self.vodml_type = vodml_element
            self.vodml_element = None
        else :
            self.vodml_type = vodml_element.vodml_type
            self.vodml_element = vodml_element


        self.vodmlid = vodmlid
        self.vodml_constraints = VodmlConstraintDict()
        self.array_size = array_size
        self.is_reference = is_reference

    def __str__(self):
        retour =  "ATTRIBUTE "
        retour += "(array_size " + str(self.array_size) + ") "
        retour += " vodmlid=" + self.vodmlid 
        if self.vodml_type:
            retour += " datatype=" + self.vodml_type
        else: 
            retour += " no dadatype"
        return retour
    def __repr__(self):
        return self.__str__()
    



class VodmlImport:
    def __init__(self, name, url):
        self.name = name
        self.url = url
    def __str__(self):
        retour =  "IMPORT " + self.name + " " + self.url +"\n"
        return retour
    def __repr__(self):
        retour =  "IMPORT " + self.name + " " + self.url +"\n"
        return retour