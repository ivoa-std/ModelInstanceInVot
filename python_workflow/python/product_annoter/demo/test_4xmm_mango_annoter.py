'''
Apply the JSON mapping descriptor for the XMM catalog to the XMM VOTABLE 
Created on 15 avr. 2020

@author: laurentmichel
'''
import os, sys
import json
file_path = os.path.dirname(os.path.realpath(__file__)) + "/../../"
if file_path not in sys.path:
    sys.path.append(file_path )

from demo import data_dir
from demo import logger  

from product_annoter.mapper.position_appender import PositionAppender  
from product_annoter.mapper.status_appender import StatusAppender  
from product_annoter.mapper.votable_merger import VOTableMerger
from product_annoter.mapper.identifier_appender import IdentifierAppender
from product_annoter.mapper.photometry_appender import PhotometryAppender
from product_annoter.mapper.genericmeasure_appender  import GenericAppender
from product_annoter.mapper.hardnessratio_appender  import HardnessRatioAppender
from product_annoter.mapper.detectionflag_appender import DetectionFlagAppender
      
if __name__ == '__main__':
        base_path = os.path.dirname(os.path.realpath(__file__)) 

        raw_votable_path = os.path.join(
            data_dir, 
            "raw_data", 
            "xmm_detections.xml")  
        annot_votable_path = os.path.join(
            data_dir, 
            "annotated_data", 
            "4xmm_detections.annot.xml")
        mango_path = os.path.join(
            data_dir, 
            "mapping_components", 
            "mango.mapping.xml")  
        component_path = os.path.join(
            data_dir, 
            "mapping_components")
        output_mapping_path = os.path.join(
            data_dir, 
            "annotated_data", 
            "4xmm_detections.mapping.xml")
        
        with open(data_dir + '/product_configs/4xmm.mango.config.json') as json_file:
            data = json.load(json_file)
           
        appender = IdentifierAppender(mango_path)
            
        appender.append_measure(data)
        appender.save(output_mapping_path)
 
        for measure in data["parameters"]:
            appender = None
            
            if measure["measure"] == "LonLatSkyPosition":
                logger.info("Position found")
                appender = PositionAppender(output_mapping_path, component_path)
            elif measure["measure"] == "status":
                logger.info("Status found")
                appender = StatusAppender(output_mapping_path, component_path)
            elif measure["measure"] == "Photometry":
                logger.info("Photometry found")
                appender = PhotometryAppender(output_mapping_path, component_path)               
            elif measure["measure"] == "GenericMeasure":
                logger.info("GenericMeasure found")
                appender = GenericAppender(output_mapping_path, component_path)
            elif measure["measure"] == "HardnessRatio":
                logger.info("GenericMeasure found")
                appender = HardnessRatioAppender(output_mapping_path, component_path)
            elif measure["measure"] == "DetectionFlag":
                logger.info("DetectionFlag found")
                appender = DetectionFlagAppender(output_mapping_path, component_path)
                
            if appender is not None:
                appender.append_measure(measure)
                #print(appender.tostring())
                appender.save(output_mapping_path)

       
        merger = VOTableMerger(raw_votable_path, output_mapping_path, annot_votable_path)
        merger.insert_mapping()