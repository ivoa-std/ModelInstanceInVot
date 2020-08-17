'''
Apply the JSON mapping descriptor for the XMM catalog to the XMM VOTABLE 
Created on 15 avr. 2020

@author: laurentmichel
'''
import os, sys
import json
file_path = os.path.dirname(os.path.realpath(__file__)) + "/../"
if file_path not in sys.path:
    sys.path.append(file_path )

from demo import data_dir
from demo import logger  

from product_annoter.mapper.position_appender import PositionAppender  
from product_annoter.mapper.status_appender import StatusAppender  
from product_annoter.mapper.votable_merger import VOTableMerger
      
if __name__ == '__main__':
        base_path = os.path.dirname(os.path.realpath(__file__)) 

        raw_votable_path = os.path.join(
            data_dir, 
            "raw_data", 
            "xmm_detections.xml")  
        annot_votable_path = os.path.join(
            data_dir, 
            "annotated_data", 
            "xmm_detections.annot.xml")
        cab_msd_path = os.path.join(
            data_dir, 
            "mapping_components", 
            "cab_msd.mapping.xml")  
        position_path = os.path.join(
            data_dir, 
            "mapping_components")
        status_path = os.path.join(
            data_dir, 
            "mapping_components", 
            "status.mapping.xml")
        output_mapping_path = os.path.join(
            data_dir, 
            "annotated_data", 
            "xmm_detections.mapping.xml")
        
        with open(data_dir + '/product_configs/xmm.config.json') as json_file:
            data = json.load(json_file)
            
        for measure in data["parameters"]:
            if measure["measure"] == "position":
                logger.info("Position found")
                appender = PositionAppender(cab_msd_path, position_path)
                appender.append_measure(measure)
                #print(appender.tostring())
                appender.save(output_mapping_path)
            elif measure["measure"] == "status":
                logger.info("Status found")
                appender = StatusAppender(output_mapping_path, status_path)
                appender.append_measure(measure)
                #print(appender.tostring())
                appender.save(output_mapping_path)
        
        merger = VOTableMerger(raw_votable_path, output_mapping_path, annot_votable_path)
        merger.insert_mapping()