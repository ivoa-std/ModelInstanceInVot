'''

Read an annotated VOTABLE and show different outputs
Created on 31 mars 2020

@author: laurentmichel
'''

import os, json, sys
from utils.json_encoder import MyEncoder
from utils.dict_utils import DictUtils

from client.launchers.instance_from_votable import InstanceFromVotable
from tests import data_dir

if __name__ == '__main__':
    base_path = os.path.dirname(os.path.realpath(__file__)) 
    votable_path = os.path.join(data_dir, 
                                "annotated_data",
                                "vizier_votable_avecActivity_Vo-dml-lite.xml"
                                )
    instance_from_votable = InstanceFromVotable(votable_path)
    instance = instance_from_votable.build_instance(resolve_refs=True)
    print(DictUtils.get_pretty_json(instance.json))
    print("=== Mapping of the columns")
    print(instance.get_flatten_data_head())
    #print(instance.get_data_subset_keys())
    print("=== First row: flatten mode")
    while True:
        inst = instance._get_next_flatten_row()
        if inst != None:
            print(DictUtils.get_pretty_json(inst))
            break
        else:
            break

    print("=== Second row: instance mode")
    while True:
        inst = instance._get_next_row_instance()
        if inst != None:
            print(DictUtils.get_pretty_json(inst))
            break
        else:
            break



    
    


    
    
    
