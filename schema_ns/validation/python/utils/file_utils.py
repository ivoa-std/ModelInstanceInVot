'''
Created on 2021/07/01

@author: laurentmichel
'''

import os

class FileUtils(object):
    file_path = os.path.dirname(os.path.realpath(__file__)) 

    @staticmethod
    def get_datadir():
        return os.path.realpath(os.path.join(FileUtils.file_path, "../../", "snippets"))
    
    @staticmethod
    def get_projectdir():
        return os.path.realpath(os.path.join(FileUtils.file_path, "../../"))
    
    @staticmethod
    def get_schemadir():
        return os.path.realpath(os.path.join(FileUtils.file_path, "../../../", "xsd"))
    