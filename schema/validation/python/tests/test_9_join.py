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
            '9.1': 'VALID',                                    # missing tableref (ok if only 1 table?)
            '9.2': '(./@tableref) and (./@dmref)',             # missing dmref
            '9.3': 'exception string',                         # empty - must have dmref or tableref
            '9.4': 'VALID',                                    # dmref + tableref
            '9.5': 'VALID',                                    # dmref + no tableref + WHERE
            '9.6': 'VALID',                                    # no dmref + tableref + WHERE
            '9.7': 'if (./@dmref) then  @dmref != \'\'',       # dmref must not be empty
            '9.8': 'if (./@tableref) then  @tableref != \'\'', # tableref must not be empty
            }

class Test(unittest.TestCase):

    def testOK(self):
        self.assertTrue(TestRunner.regarde_si_OK(mapping_sample, "test_9"), "file should be valid")

    def testKO(self):
        self.assertTrue(TestRunner.regarde_si_KO(mapping_sample, "test_9", expected), "invalid file test failed.")


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
