import sys, os
from utils.logger_setup import LoggerSetup


file_path = os.path.dirname(os.path.realpath(__file__)) 


data_dir = os.path.join(file_path, "../../..", "data")
logger = LoggerSetup.get_logger()
LoggerSetup.set_info_level()
