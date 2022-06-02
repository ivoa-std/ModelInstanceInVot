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
            '6.1': 'VALID',
            '6.2': 'VALID',
            '6.3': '(./@dmref and not(./@sourceref)) or (not(./@dmref) and ./@sourceref)',
            '6.4': '(./@dmref and not(./@sourceref)) or (not(./@dmref) and ./@sourceref)',
            '6.5': 'every $child in ./dm-mapping:REFERENCE satisfies  $child/@dmrole != \'\'',
            '6.6': '((count(dm-mapping:FOREIGN_KEY) &gt; 0 and ./@sourceref and not(./@dmref))',
            '6.7': '(count(./dm-mapping:FOREIGN_KEY) eq 0 and not(./@sourceref) and ./@dmref))',
            '6.8': 'VALID',
            '6.9': 'every $child in ./dm-mapping:REFERENCE satisfies  $child/@dmrole != \'\'',
            '6.10': 'if (./@sourceref) then  @sourceref != \'\'',
            '6.11': 'if (./@dmref) then  @dmref != \'\'',
            '6.12': 'VALID',
            '6.13': 'VALID',
            '6.14': 'count (dm-mapping:REFERENCE[@dmrole != \'\']) eq 0',
            }

class Test(unittest.TestCase):

    def testOK(self):
        self.assertTrue(TestRunner.regarde_si_OK(mapping_sample, "test_6"), "file should be valid")

    def testKO(self):
        self.assertTrue(TestRunner.regarde_si_KO(mapping_sample, "test_6", expected), "invalid file test failed.")


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
