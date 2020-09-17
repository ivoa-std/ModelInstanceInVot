import sys, os

file_path = os.path.dirname(os.path.realpath(__file__)) + "/../../"
if file_path not in sys.path:
    sys.path.append(file_path )

from utils.logger_setup import LoggerSetup


data_dir = os.path.join(file_path, "..", "data")
sample_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")

logger = LoggerSetup.get_logger()
LoggerSetup.set_debug_level()

# make sure to know where we are to avoid issue with relative paths
os.chdir(os.path.dirname(os.path.realpath(__file__)))

#Config.__read_config__(config_file)
logger.info("product_anoter.tests package initialized")