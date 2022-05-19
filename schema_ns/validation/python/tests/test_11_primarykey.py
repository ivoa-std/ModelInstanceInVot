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
            '11.1': 'VALID',
            '11.2': 'VALID',
            '11.3': './@ref  or ./@value',
            '11.4': '(./@value and not(./@ref)) or (not(./@value) and ./@ref)',
            '11.5': '@dmtype != \'\'',
            '11.6': '@dmtype != \'\'',
            '11.7': 'if (./@ref) then  @ref != \'\'',
            '11.8': 'VALID',
            }

class Test(unittest.TestCase):

    def testOK(self):
        self.assertTrue(TestRunner.regarde_si_OK(mapping_sample, "test_11"), "file should be valid")

    def testKO(self):
        self.assertTrue(TestRunner.regarde_si_KO(mapping_sample, "test_11", expected), "invalid file test failed.")


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
