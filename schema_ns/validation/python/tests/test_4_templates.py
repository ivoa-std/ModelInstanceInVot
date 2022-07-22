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
            '4.1': 'VALID',
            '4.2': 'VALID',
            '4.3': 'The content of element \'dm-mapping:TEMPLATES\' is not complete. Tag \'dm-mapping:INSTANCE\' expected.',
            '4.4': 'Unexpected child with tag \'dm-mapping:WHERE\' at position 2.',
            '4.5': 'VALID',
            '4.6': 'VALID',
            '4.7': 'Unexpected child with tag \'dm-mapping:BANDOL\' at position 1. Tag \'dm-mapping:INSTANCE\' expected.',
            '4.8': 'VALID',
            '4.9': 'if (@tableref) then (@tableref != \'\')',
            }

class Test(unittest.TestCase):

    def testOK(self):
        self.assertTrue(TestRunner.regarde_si_OK(mapping_sample, "test_4"), "file should be valid")

    def testKO(self):
        self.assertTrue(TestRunner.regarde_si_KO(mapping_sample, "test_4", expected), "invalid file test failed.")


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
