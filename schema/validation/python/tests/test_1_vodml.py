'''
Created on 2021/07/01

@author: laurentmichel
'''
import unittest
from utils.file_utils import FileUtils
from utils.test_runner import TestRunner

mapping_sample = FileUtils.get_datadir()
 
# Expected results
expected = {
            '1.1': 'VALID',
            '1.2': 'VALID',
            '1.3': 'VALID',
            '1.4': 'VALID',
            '1.5': 'Tag \'dm-mapping:MODEL\' expected.',
            '1.6': 'Unexpected child with tag \'dm-mapping:GLOBALS\' at position 1. Tag \'dm-mapping:MODEL\' expected.',
            '1.7': 'Unexpected child with tag \'dm-mapping:GLOBALS\' at position 3.',
            '1.8': 'VALID',
            '1.9': 'VALID',
            '1.10': 'Unexpected child with tag \'dm-mapping:GLOBALS\' at position 3.',
            '1.11': 'Unexpected child with tag \'dm-mapping:BEAUJOLAIS\'',
            }

class Test(unittest.TestCase):

    def testOK(self):
        self.assertTrue(TestRunner.regarde_si_OK(mapping_sample, "test_1"), "file should be valid")

    def testKO(self):
        self.assertTrue(TestRunner.regarde_si_KO(mapping_sample, "test_1", expected), "invalid file test failed.")


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
