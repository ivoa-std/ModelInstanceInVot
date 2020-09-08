from lxml import etree
import sys
import xml.dom.minidom
from mapping_factory.factory.model_constraints import *
from mapping_factory.factory.model_components import *
from mapping_factory import logger

import urllib.request
import copy
from email.policy import default
class ModelMapper:
    def __init__(self, filename,model=None):
        self.filename = filename
        self.model = model
        self.data_types = dict()
        self.object_types = dict()
        self.imports = dict()
        self.primitive_types = dict()
        self._parse_imports(self.filename)
        self.xml_string = ""
        self.type_filter = dict()
        self.value_filter = dict()
        
    def _get_vodml_element(self, vodml_type):
        if vodml_type in self.object_types.keys() :
            return self.object_types[vodml_type]
        elif vodml_type in self.data_types.keys():
            return self.data_types[vodml_type]
        else:
            logger.warning("type " + vodml_type + " not on objet/data_types")
            return None

    def _append_xml(self, string):
        self.xml_string +=  string 
        return

    def _parse_imports(self, filename):
        if filename.startswith("http://") or filename.startswith("https://") :
            tree = etree.ElementTree(file=urllib.request.urlopen(filename))
        else :
            tree = etree.parse(filename)
                
        root = tree.getroot()
        name =  root.find("name").text
        if not name in self.imports.keys():
            logger.info(" add file " + name + " " + filename)
            self.imports[name]=filename
                
        for node in tree.xpath("import"):
            name = node.find('name').text
            url = node.find('url').text
            if not name in self.imports:
                if not name in self.imports.keys():
                    logger.info(" add file " + name + " " + url)
                    self.imports[name]=url



           
    def _parse_vodml_file(self, filename):
    
        if self.filename.startswith("http://") or self.filename.startswith("https://") :
            tree = etree.ElementTree(file=urllib.request.urlopen(filename))
        else :
            tree = etree.parse(filename)

        root = tree.getroot()
        model_name =  root.find("name").text
    
        logger.info("Reading FILE " + filename + " for model " + model_name)
    
        for node in tree.xpath("*"):
            if node.tag == 'package':
                self.read_package(model_name, node)
            elif node.tag == 'primitiveType'  or node.tag == 'enumeration':
                dt = self.read_data_type(model_name, node)
                logger.info("ADD primitiveType " + dt.vodml_type)
                self.primitive_types[dt.vodml_type] = dt
            elif node.tag == 'dataType' or node.tag == 'reference':
                dt = self.read_data_type(model_name, node)
                logger.info("ADD dataType " + dt.vodml_type)
                self.data_types[dt.vodml_type] = dt
            elif node.tag == 'objectType':
                dt = self.read_object_type(model_name, node)
                logger.info("ADD objectType " + dt.vodml_type)
                self.object_types[dt.vodml_type] = dt
    
    def _resolve_constraints(self):
        for obj in  self.data_types.values():
            self._resolve_constraint(obj)
        for obj in  self.object_types.values():
            self._resolve_constraint(obj)

    def _resolve_constraint(self, vodml_component):
        logger.info("_resolve_constraint for " + vodml_component.vodml_type)
        for att_type, const in vodml_component.vodml_constraints.items():
            if const.is_subset:
                logger.info("add subset " + const.__repr__() + " to " + vodml_component.vodml_type)
                att = vodml_component.attributes[att_type]
                att.vodml_type = const.subset
                att.vodml_component = None
        
   
    def _resolve_inheritances(self):
        for obj in  self.data_types.values():
            self._resolve_inheritance(obj)
        for obj in  self.object_types.values():
            self._resolve_inheritance(obj)
                  
    def _resolve_inheritance(self, vodml_component):
        logger.info("resolve_inheritance for " + vodml_component.vodml_type)
        nb_att0 = len(vodml_component.attributes)

        while vodml_component.superclass != '':
            sup_obj= None
            logger.info("  merge att of " + vodml_component.superclass)

            if vodml_component.superclass in self.data_types :
                sup_obj = self.data_types[vodml_component.superclass]
            elif vodml_component.superclass in self.object_types :
                sup_obj = self.object_types[vodml_component.superclass]
            elif vodml_component.superclass in self.primitive_types :
                sup_obj = self.primitive_types[vodml_component.superclass]
            else:
                logger.error( vodml_component.superclass + " Neither in dataType nor in primitive types")
                sys.exit()
            for k,v in sup_obj.attributes.items():
                vodml_component.attributes[k] = v
            vodml_component.superclass = sup_obj.superclass
        nb_att1 = len(vodml_component.attributes)
        if nb_att0 != nb_att1 :
            logger.info("resolve_inheritance: " + vodml_component.vodml_type + " " + str(nb_att0) + "->" + str(nb_att1) + " atts")

            #for k,v in sup_obj.vodml_constraints.constraints.items():
            #    print(sup_obj.vodml_constraints.constraints)
            #    obj.vodml_constraints.merge(v)
            superclass = sup_obj.superclass
            
    def set_type_filter(self, type_filter):
        self.type_filter = type_filter
    def value_type_filter(self, value_filter):
        self.value_filter = value_filter

    def parse_vodml_files(self):
        for model, url in self.imports.items():
            logger.info("parse " + model + " " + url)
            self._parse_vodml_file(url)
        self._resolve_inheritances()
        self._resolve_constraints()

    def read_package(self, model_name, package_node):
        if package_node.tag == 'package':
            package_name =  package_node.find("name").text
            logger.info ("read_package" , "Reading package " + package_name)
            for child in package_node.findall('*'):
                if child.tag == "objectType":
                    ot = self.read_object_type(model_name, child)
                    logger.info("ADD OBJECT " + ot.__repr__())
                    self.object_types[ot.vodmlid] = ot
                elif child.tag == 'primitiveType'   or child.tag == 'enumeration':
                    dt = self.read_data_type(model_name, child)
                    logger.info("ADD PRIM TYPE " + dt.__repr__())
                    self.primitive_types[dt.vodmlid] = dt
                elif child.tag == "dataType" :
                    ot = self.read_data_type(model_name, child)
                    logger.info("ADD DATA TYPE " + ot.__repr__())
                    self.data_types[ot.vodmlid] = ot
                elif child.tag == 'package':
                    self.read_package(model_name, child)

    def read_data_type(self, model_name,datatype_tag):
        vodml_type = ''
        name = ''
        superclass = ''
        ref = ''
        attributes = dict()
        constraints = VodmlConstraintDict()
        abstract = False
        if datatype_tag.get("abstract") == "true":
            abstract = True
        for datatype_tag_child in datatype_tag.findall('*'):
            if datatype_tag_child.tag == "vodml-id":
                vodml_type = model_name + ":" + datatype_tag_child.text
                logger.info("READING DATA TYPE " + vodml_type)

            elif datatype_tag_child.tag == "name":
                name = datatype_tag_child.text
            elif datatype_tag_child.tag == "vodml-ref":
                ref = datatype_tag_child.text
            elif datatype_tag_child.tag == "attribute" or datatype_tag_child.tag == "reference" :
                att = self.read_attribute(datatype_tag_child, model_name)
                attributes[att.vodmlid] = att
            elif datatype_tag_child.tag == "extends":
                for super_type_child in datatype_tag_child.findall('vodml-ref'):
                    superclass = super_type_child.text
                    break
            elif datatype_tag_child.tag == "constraint":
                ct = self.read_constraint(datatype_tag_child)
                constraints.add_contraint(ct)
 
            elif datatype_tag_child.tag == "reference":
                att = self.read_reference(model_name,datatype_tag_child)
                attributes[att.vodmlid] = att

        retour = VodmlDataType(vodml_type, superclass, attributes, constraints, ref=ref, abstract=abstract)
        return retour

         
         
     
    def read_reference(self, model_name,reference_tag):
        for reference_tag_child in reference_tag.findall('*'):
            if reference_tag_child.tag == "vodml-id":
                vodmlid = model_name + ":" + reference_tag_child.text
            elif reference_tag_child.tag == "name":
                name = reference_tag_child.text
            elif reference_tag_child.tag == "datatype":
                for vodml_ref_tag_child in reference_tag_child.findall('vodml-ref'):
                    dmtype = vodml_ref_tag_child.text                
                
        return VodmlAttribute(vodmlid, dmtype, True, array_size=1)

    def read_constraint(self, constraint_tag):  
        role=""
        datatype = ""  
        description=""
        for constraint_tag_child in constraint_tag.findall('*'):
            # subset
            if constraint_tag_child.tag == "role":
                for constraint_tag_sub_child in constraint_tag_child.findall('*'):
                    if constraint_tag_sub_child.tag == "vodml-ref":
                        role = constraint_tag_sub_child.text
                        break

            elif constraint_tag_child.tag == "datatype":
                for constraint_tag_sub_child in constraint_tag_child.findall('*'):
                    if constraint_tag_sub_child.tag == "vodml-ref":
                        datatype = constraint_tag_sub_child.text
                        break
            elif constraint_tag_child.tag == "description":
                description = constraint_tag_child.text
        
        vodml_contraint = VodmlConstraint(role, datatype, description)
        return vodml_contraint        

     
    def read_object_type(self, model_name, object_type_tag):
        attributes = dict()
        constraints = VodmlConstraintDict()
        superclass = ''
    
        abstract = False
        if object_type_tag.get("abstract") == "true":
            abstract = True
        for object_type_child in object_type_tag.findall('*'):
            if object_type_child.tag == "vodml-id":
                vodml_type = model_name + ":" + object_type_child.text
                logger.info("READING OBJECT TYPE " + vodml_type)
   
            elif object_type_child.tag == "name":
                name = object_type_child.text
            elif object_type_child.tag == "composition" or object_type_child.tag == "attribute" :
                #or multiplicity_tag_child in object_type_child.findall('maxOccurs'):
                #    array_size = int(multiplicity_tag_child.text)
                att = self.read_attribute(object_type_child, model_name)
                attributes[att.vodmlid] = att
            elif object_type_child.tag == "extends":
                for super_type_child in object_type_child.findall('vodml-ref'):
                    superclass = super_type_child.text
                    break
            elif object_type_child.tag == "reference":
                att = self.read_reference(model_name,object_type_child)
                attributes[att.vodmlid] = att

            elif object_type_child.tag == "constraint":
                ct = self.read_constraint(object_type_child)
                constraints.add_contraint(ct)
        retour = VodmlObjectType(vodml_type, superclass, attributes, constraints, abstract=abstract)

 
        return retour    
    
    def read_attribute(self,attribute_tag, model_name):
        dmtype = ''
        arraysize = 2
        vodml_element = None
        logger.info("Parsing attribute")
        #print(etree.dump(attribute_tag))
        for attribute_tag_child in attribute_tag.findall('*'):
            if attribute_tag_child.tag == "vodml-id":
                vodmlid = model_name + ":" + attribute_tag_child.text
            elif attribute_tag_child.tag == "name":
                name = attribute_tag_child.text
            elif attribute_tag_child.tag == "multiplicity":
                for multiplicity_tag_child in attribute_tag_child.findall('maxOccurs'):
                    arraysize = int(multiplicity_tag_child.text)
            elif attribute_tag_child.tag == "datatype" or attribute_tag_child.tag == 'reference':
                for vodml_ref_tag_child in attribute_tag_child.findall('vodml-ref'):
                    dmtype = vodml_ref_tag_child.text  
                    break
                if dmtype in self.object_types.keys():
                    vodml_element = copy.copy(self.object_types[dmtype])
                elif dmtype in self.data_types.keys():
                    vodml_element = copy.copy(self.data_types[dmtype])
        retour = VodmlAttribute(vodmlid, dmtype, False, array_size=arraysize)
        return retour
    

    def generate_mapping(self, vodml_root_type):
        self.xml_string = ""
        logger.info("Generate mapping fotr " + vodml_root_type.vodml_type)
        self._append_xml("<MODEL_INSTANCE>")
        self._append_xml("<MODELS>")
        for k,v in self.imports.items():
            self._append_xml("<MODEL>")
            self._append_xml("<NAME>" + k + "</NAME>")
            self._append_xml("<URL>" + v + "</URL>")
            self._append_xml("</MODEL>")
        self._append_xml("</MODELS>")
        self._append_xml("<GLOBALS>")
        self._append_xml("</GLOBALS>")
        self._append_xml("<TABLE_MAPPING tableref='Results' >")
        self.generate_object_mapping("root", vodml_root_type)
        self._append_xml("</TABLE_MAPPING>")
        self._append_xml("</MODEL_INSTANCE>")
        
    def generate_object_mapping(self, vodml_role,vodml_object_type):
        
        if vodml_object_type.vodml_constraints.get_nosubset_constraint() :
            ctr = " const='" + vodml_object_type.vodml_constraints.get_nosubset_constraint().description + "' "
        else:
            ctr = ""
            
        if vodml_object_type.abstract :
            abstr = " abstr='true' "
        else:
            abstr = ""
        str = "<INSTANCE dmrole='" + vodml_role + "' dmtype='" + vodml_object_type.vodml_type + "' " + abstr + ctr + ">"
        self._append_xml(str)


        for attribute in vodml_object_type.attributes.values():
            if attribute.vodml_type in self.type_filter:
                attribute.vodml_type = self.type_filter[attribute.vodml_type]
            self.generate_attribute_mapping(attribute)
                #print( "SKIPPP " + attribute.vodmlid )
        self._append_xml( "</INSTANCE>")
        
    def generate_attribute_mapping(self, attribute):
 
        if attribute.vodmlid in self.value_filter.keys():
            default = " default='" + self.value_filter[attribute.vodmlid] + "' "
        else :
            default = ""

        if attribute.array_size == 0 :
            return
        
 
        elif attribute.array_size == 1:
            att_element = self._get_vodml_element(attribute.vodml_type)  
            if att_element :              
                self.generate_object_mapping(attribute.vodmlid, att_element)
            else:
                self._append_xml( "<ATTRIBUTE dmrole='" + attribute.vodmlid +  "' dmtype='" + attribute.vodml_type +  "' ref='@@@@@@' " + default + "/>")

        elif attribute.array_size == -1:
            #sys.exit(1)
            self._append_xml( "<COLLECTION  size='-1'>")   
            att_element = self._get_vodml_element(attribute.vodml_type)  
            if att_element :              
                self.generate_object_mapping(attribute.vodmlid, att_element)
            else:
                self._append_xml( "<ATTRIBUTE dmrole='" + attribute.vodmlid +  "' ref='@@@@@@' " + default + " />")
            
            self._append_xml( "</COLLECTION>")
        else:
            self._append_xml( "<COLLECTION  size='" + str(attribute.array_size) + "'>")
            for i in range(0,attribute.array_size ):
                pass
            #for num in range(0, attribute.array_size):
            #    print("======== add " + attribute.__repr__())
            #    self.generate_single_attribute_mapping(attribute)
            self.append_xml( "</COLLECTION>")
            
                    
    def map_object_type(self, object_type):
        logger.info("map object " + object_type)
        if object_type in self.object_types.keys():
            retour = copy.copy(self.object_types[object_type])
        elif object_type in self.data_types.keys():
            retour = copy.copy(self.data_types[object_type])  
        self.generate_mapping(retour)

        return retour
          


    def list_data_types(self):
        for k in self.data_types:
            print("data type key: " + k + " " + self.data_types[k].vodml_type)    
               
    def list_object_types(self):
        for k in self.object_types:
            print("object type key: " + k + " " + self.object_types[k].vodml_type)
                
def main():
    mapping_generator = ModelMapper("https://volute.g-vo.org/svn/trunk/projects/dm/STC/Meas/vo-dml/STC_meas-v1.0.vo-dml.xml", model='meas')
    mapping_generator.parse_vodml_files()
    mapping_generator.list_data_types()
    mapping_generator.list_object_types()
    # type => type
    mapping_generator.set_type_filter({"ivoa:Quantity": "ivoa:RealQuantity"
                                       , "coords:RefLocation": "coords:StdRefLocation"
                                       , "meas:Uncertainty": "meas:Symmetrical"
                                       , "coords:Coordinate": "coords:GenericCoordValue"
    })
    # role => value
    #mapping_generator.value_type_filter({"coords:SpaceFrame.spaceRefFrame": "ICRS"
    #                                    , "coords:StdRefLocation.position": "GEOCENTER"
    #                                    , "coords:SpaceFrame.equinox": "J2000"
    #})
    mapping_generator.map_object_type('meas:GenericMeasure')
    #print(mapping_generator.xml_string)
    xmld = xml.dom.minidom.parseString(mapping_generator.xml_string + "\n")
    xml_pretty_str = xmld.toprettyxml(indent="  ")
    print(xml_pretty_str)
    sys.exit()

    mapping_generator.value_type_filter({"coords:SpaceFrame.spaceRefFrame": "ICRS"
                                        , "coords:StdRefLocation.position": "BARYCENTER"
                                        , "coords:TimeFrame.timescale": "TT"
    })
    mapping_generator.map_object_type('coords:TimeFrame')
    #print(mapping_generator.xml_string)
    xmld = xml.dom.minidom.parseString(mapping_generator.xml_string + "\n")
    xml_pretty_str = xmld.toprettyxml(indent="  ")
    print(xml_pretty_str)

if __name__ == "__main__":
    main()   
    sys.exit()  