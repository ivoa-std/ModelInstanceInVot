'''
Created on 15 avr. 2020

@author: laurentmichel
'''
import os
from product_annoter.mapper.constants import PARAM_TEMPLATES
from product_annoter.mapper.parameter_appender import ParameterAppender

class PositionAppender:
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
                                          "mango.LonLatSkyPosition.mapping.xml")
        self.appender = ParameterAppender(
            PARAM_TEMPLATES.POSITION,
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
        
        self.set_spaceframe(measure_descriptor["frame"]["frame"],
                            measure_descriptor["frame"]["equinox"])
        self.set_position(measure_descriptor["position"]["longitude"], 
                          measure_descriptor["position"]["latitude"]
                          ) 
        self.set_errors(measure_descriptor["errors"]["random"]["value"], 
                        measure_descriptor["errors"]["random"]["unit"], 
                        measure_descriptor["errors"]["systematic"]["value"], 
                        measure_descriptor["errors"]["systematic"]["unit"] 
                        ) 
        self.set_notset_value()
        
    def set_spaceframe(self, frame, equinox):   
        with open(os.path.join(self.component_path, "mango.frame." + frame + ".xml")) as xml_file:
            data = xml_file.read()
            self.appender.add_globals_xx(data)
            self.appender.set_dmref("coords:Coordinate.coordSys", "SpaceFrame_" + frame)
        return
             
    def set_position(self, ra_ref, dec_ref):
        self.appender.set_ref_or_value("mango:stcextend.LonLatSkyPosition.coord", 
                              "mango:stcextend.LonLatPoint.longitude", 
                              ra_ref)
        self.appender.set_ref_or_value("mango:stcextend.LonLatSkyPosition.coord", 
                              "mango:stcextend.LonLatPoint.latitude", 
                              dec_ref)
                                     
    def set_errors(self, err_ref , err_unit, sys_err_ref, sys_err_unit):
        if err_ref is not None:
            self.appender.set_ref_or_value("meas:Error.statError", 
                                  "ivoa:RealQuantity.value", 
                                  err_ref)
        
            self.appender.set_ref_or_value("meas:Error.statError", 
                                    "ivoa:Quantity.unit", 
                                    err_unit)
        if sys_err_ref is not None:
            self.appender.set_ref_or_value("meas:Error.sysError", 
                                  "ivoa:RealQuantity.value", 
                                  sys_err_ref)
        
            self.appender.set_ref_or_value("meas:Error.sysError", 
                                   "ivoa:Quantity.unit", 
                                sys_err_unit)
            
    def set_param_semantic(self, ucd, semantic, description):
        self.appender.set_param_semantic(ucd, semantic, description) 


    def set_notset_value(self):
        self.appender.set_notset_value()
        
    def tostring(self):
        return self.appender.tostring()
        
    def save(self, output_path):
        self.appender.save(output_path)

        
