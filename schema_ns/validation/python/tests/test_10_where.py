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
            '10.1': '(./@foreignkey and ./@primarykey and not(@value)) or (./@foreignkey and not(./@primarykey) and @value)  or (not(./@foreignkey) and ./@primarykey and @value)',
            '10.2': 'VALID',
            '10.3': 'VALID',
            '10.4': 'VALID',
            '10.5': '(./@foreignkey and ./@primarykey and not(@value)) or (./@foreignkey and not(./@primarykey) and @value)  or (not(./@foreignkey) and ./@primarykey and @value)',
            '10.6': '(./@foreignkey and ./@primarykey and not(@value)) or (./@foreignkey and not(./@primarykey) and @value)  or (not(./@foreignkey) and ./@primarykey and @value)',
            '10.7': '(./@foreignkey and ./@primarykey and not(@value)) or (./@foreignkey and not(./@primarykey) and @value)  or (not(./@foreignkey) and ./@primarykey and @value)',
            '10.8': '(./@foreignkey and ./@primarykey and not(@value)) or (./@foreignkey and not(./@primarykey) and @value)  or (not(./@foreignkey) and ./@primarykey and @value)',
            '10.9': 'if (./@primarykey) then  @primarykey != \'\'',
            '10.10': 'if (./@foreignkey) then  @foreignkey != \'\'',
            '10.11': 'VALID',
            }

class Test(unittest.TestCase):

    def testOK(self):
        self.assertTrue(TestRunner.regarde_si_OK(mapping_sample, "test_10"), "file should be valid")

    def testKO(self):
        self.assertTrue(TestRunner.regarde_si_KO(mapping_sample, "test_10", expected), "invalid file test failed.")


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
