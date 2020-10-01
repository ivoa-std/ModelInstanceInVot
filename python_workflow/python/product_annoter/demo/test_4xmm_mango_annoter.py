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

from product_annoter.demo import data_dir
from product_annoter.demo import logger  

from product_annoter.mapper.position_appender import PositionAppender  
from product_annoter.mapper.status_appender import StatusAppender  
from product_annoter.mapper.votable_merger import VOTableMerger
from product_annoter.mapper.identifier_appender import IdentifierAppender
from product_annoter.mapper.photometry_appender import PhotometryAppender
from product_annoter.mapper.genericmeasure_appender  import GenericAppender
from product_annoter.mapper.hardnessratio_appender  import HardnessRatioAppender
from product_annoter.mapper.detectionflag_appender import DetectionFlagAppender
from product_annoter.mapper.mjd_appender import MJDAppender
      
if __name__ == '__main__':
        base_path = os.path.dirname(os.path.realpath(__file__)) 

        # path of the initial VOTable
        raw_votable_path = os.path.join(
            data_dir, 
            "raw_data", 
            "xmm_detections.xml")  
        # path of the annotated VOTable
        annot_votable_path = os.path.join(
            data_dir, 
            "annotated_data", 
            "4xmm_detections.annot.xml")
        # Directory with all the mapping components
        component_path = os.path.join(
            data_dir, 
            "mapping_components")
        # Path of the empty MANGO mapping block
        # This mapping block will host all parameters
        # to be mapped for this VOTable
        mango_path = os.path.join(
            component_path, 
            "mango.mapping.xml")  
        # Output file with just the mapping block
        output_mapping_path = os.path.join(
            data_dir, 
            "annotated_data", 
            "4xmm_detections.mapping.xml")
        
        # Read the mapping configuration for this VOTable.
        # This configuration lists a  parameters to be mapped 
        # with the column references or the literal values
        with open(os.path.join(data_dir, 'product_configs', '4xmm.mango.config.json')) as json_file:
            mapping_config = json.load(json_file)
        
        # set the source identifier mapping
        # This is the only mandatory source parameter  
        appender = IdentifierAppender(mango_path)
        appender.append_measure(mapping_config)
        appender.save(output_mapping_path)
 
        # Iterate upon all the parameters to be instanciated
        # The is one appender class for each parameter class
        for measure in mapping_config["parameters"]:
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
            elif measure["measure"] == "MJD":
                logger.info("MJD found")
                appender = MJDAppender(output_mapping_path, component_path)
                
            if appender is not None:
                # Build the mapping block for the current measure
                appender.append_measure(measure)
                # Save the file with just the mapping block
                appender.save(output_mapping_path)

        # Insert the mapping block in the head of the VOTable
        merger = VOTableMerger(raw_votable_path, output_mapping_path, annot_votable_path)
        merger.insert_mapping()