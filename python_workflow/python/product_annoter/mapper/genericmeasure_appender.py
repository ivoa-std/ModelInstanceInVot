'''
Created on 15 avr. 2020

@author: laurentmichel
'''
import os
from product_annoter.mapper.constants import PARAM_TABLE_MAPPING
from product_annoter.mapper.parameter_appender import ParameterAppender

class GenericAppender:
    '''
    classdocs
    '''
    
    def __init__(self, mango_path, component_path):           
        '''
        Constructor
        '''
        self.mango_path = mango_path    
        self.component_path = component_path  
        self.position_path = os.path.join(component_path, 
                                          "mango.GenericMeasure.mapping.xml")
        self.appender = ParameterAppender(
            PARAM_TABLE_MAPPING.POSITION,
            self.mango_path,
            self.position_path
            )

        #self.appender.add_globals()
        self.appender.add_param_parameter()
    
    def append_measure(self, measure_descriptor):  
        self.set_param_semantic(measure_descriptor["ucd"], 
                                measure_descriptor["semantic"],
                                measure_descriptor["description"]
                                )
        
        self.set_position(measure_descriptor["coordinate"]["value"], 
                          measure_descriptor["coordinate"]["unit"]
                          ) 
 
        self.set_notset_value()
        
             
    def set_position(self, value, unit):
        self.appender.set_ref_or_value("coords:PhysicalCoordinate.cval", 
                              "ivoa:RealQuantity.value", 
                              value)
        self.appender.set_ref_or_value("coords:PhysicalCoordinate.cval", 
                              "ivoa:RealQuantity.unit", 
                              unit)
                                      
            
    def set_param_semantic(self, ucd, semantic, description):
        self.appender.set_param_semantic(ucd, semantic, description) 


    def set_notset_value(self):
        self.appender.set_notset_value()
        
    def tostring(self):
        return self.appender.tostring()
        
    def save(self, output_path):
        self.appender.save(output_path)

        
