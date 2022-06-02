'''
Created on 2021/07/01

@author: laurentmichel
'''
import unittest
from utils.file_utils import FileUtils
from utils.test_votable_runner import TestVOTableRunner

mapping_sample = FileUtils.get_datadir()
 

class Test(unittest.TestCase):

    def testOK(self):
        self.assertTrue(TestVOTableRunner.regarde_si_OK(mapping_sample, "test_rich_instance"), "file should be valid")

    def testKO(self):
        self.assertTrue(TestVOTableRunner.regarde_si_KO(mapping_sample, "test_rich_instance"), "file shouldn't be valid")

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
