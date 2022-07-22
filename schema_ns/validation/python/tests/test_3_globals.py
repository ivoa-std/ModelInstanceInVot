'''
Created on 2021/09/18

@author: laurentmichel
'''
import unittest
from utils.file_utils import FileUtils
from utils.test_runner import TestRunner

mapping_sample = FileUtils.get_datadir()
 
# Expected results
expected = {
            '3.1': 'VALID',
            '3.2': 'VALID',
            '3.3': 'VALID',
            '3.4': 'VALID',
            '3.5': 'VALID',
            '3.6': 'Unexpected child with tag \'dm-mapping:REFERENCE\' at position 1.',
            }

class Test(unittest.TestCase):

    def testOK(self):
        self.assertTrue(TestRunner.regarde_si_OK(mapping_sample, "test_3"), "file should be valid")

    def testKO(self):
        self.assertTrue(TestRunner.regarde_si_KO(mapping_sample, "test_3", expected), "invalid file test failed.")


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
