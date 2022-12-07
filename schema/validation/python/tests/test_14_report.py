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
            '14.1': 'VALID',
            '14.2': 'VALID',
            '14.3': "@status = 'OK' or @status = 'FAILED'"
            }

class Test(unittest.TestCase):

    def testOK(self):
        self.assertTrue(TestRunner.regarde_si_OK(mapping_sample, "test_14"), "file should be valid")

    def testKO(self):
        self.assertTrue(TestRunner.regarde_si_KO(mapping_sample, "test_14", expected), "invalid file test failed.")


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
