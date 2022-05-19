'''
Created on 2021/09/17

@author: laurentmichel
'''
import unittest
from utils.file_utils import FileUtils
from utils.test_runner import TestRunner

mapping_sample = FileUtils.get_datadir()
 
# Expected results
expected = {
            '13.2': 'duplicated value (\'_sameid\',)',
            '13.1': 'duplicated value (\'_sameid\',)',
            '13.3': 'duplicated value (\'_ref2\',)',
            '13.4': 'duplicated value (\'_ref2\',)',
            '13.5': 'duplicated value (\'_sameid\',)',
            }

class Test(unittest.TestCase):

    def testOK(self):
        self.assertTrue(TestRunner.regarde_si_OK(mapping_sample, "test_13"), "file should be valid")

    def testKO(self):
        self.assertTrue(TestRunner.regarde_si_KO(mapping_sample, "test_13", expected), "invalid file test failed.")


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
