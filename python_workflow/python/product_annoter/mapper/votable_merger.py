'''
Created on 16 avr. 2020

@author: laurentmichel
'''
from product_annoter.mapper import logger
class VOTableMerger(object):
    '''
    classdocs
    '''


    def __init__(self, raw_votable_path, mapping_block_path, output_path):
        '''
        Constructor
        '''
        self.raw_votable_path = raw_votable_path
        self.mapping_block_path = mapping_block_path
        self.output_path = output_path
     
    def _get_mapping(self):
        with open(self.mapping_block_path, 'r') as mapping:
            return mapping.read()
           
    def insert_mapping(self):
        logger.info("save annotatedVOTable in %s", self.output_path)
        with open(self.output_path, 'w') as output_votable:            
            with open(self.raw_votable_path, 'r') as raw_votable:
                for line in raw_votable:
                    output_votable.write(line)
                    if line.startswith("<VOTABLE") is True:
                        output_votable.write(self._get_mapping())

