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
            '7.1': 'VALID',
            '7.2': 'VALID',
            '7.3': 'VALID',
            '7.4': '(not(./@ref) and ./@value) or (not(./@value) and ./@ref) or (./@value and ./@ref)',
            '7.5': 'VALID',
            '7.6': 'VALID',
            '7.7': 'VALID',
            '7.8': 'if (./@arrayindex) then (./@ref)',
            '7.9': 'every $child in ./dm-mapping:ATTRIBUTE satisfies  $child/@dmrole != \'\'',
            '7.10': 'missing required attribute \'dmtype\'',
            '7.11': 'every $child in ./dm-mapping:ATTRIBUTE satisfies  $child/@dmrole != \'\'',
            '7.12': '@dmtype != \'\'',
            '7.13': 'if (@ref) then (@ref != \'\')',
            '7.14': 'VALID',
            '7.15': 'if (@arrayindex) then (@arrayindex &gt;= \'0\')',
            '7.16': 'count (dm-mapping:ATTRIBUTE[@dmrole != \'\']) eq 0',
            '7.17': 'VALID',
            '7.18': 'VALID',
            '7.19': 'VALID',
            '7.20': 'VALID',
            '7.21': 'VALID',
            #'7.22': "every $child in .//dm-mapping:ATTRIBUTE satisfies (not($child/@ref) or $child/@ref = '')",
            '7.22': "if (@ref) then (@ref != '') else true() " 
            }

class Test(unittest.TestCase):

    def testOK(self):
        self.assertTrue(TestRunner.regarde_si_OK(mapping_sample, "test_7"), "file should be valid")

    def testKO(self):
        self.assertTrue(TestRunner.regarde_si_KO(mapping_sample, "test_7", expected), "invalid file test failed.")


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
