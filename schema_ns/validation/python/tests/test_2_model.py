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
            '2.1': 'VALID',
            '2.2': 'VALID',
            '2.3': '@name != \'\'',
            '2.4': '@name != \'\'',
            '2.5': 'if (@url) then (@url != \'\')',
            }

class Test(unittest.TestCase):

    def testOK(self):
        self.assertTrue(TestRunner.regarde_si_OK(mapping_sample, "test_2"), "file should be valid")

    def testKO(self):
        self.assertTrue(TestRunner.regarde_si_KO(mapping_sample, "test_2", expected), "invalid file test failed.")


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
