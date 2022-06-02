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
            '5.1': 'count (dm-mapping:INSTANCE[@dmrole != \'\']) eq 0',
            '5.2': 'count (dm-mapping:INSTANCE[@dmrole != \'\']) eq 0',
            '5.3': 'VALID',
            '5.4': 'VALID',
            '5.5': 'VALID',
            '5.6': 'VALID',
            '5.7': 'if (@dmid) then ( @dmid != \'\')',
            '5.8': 'missing required attribute \'dmtype\'',
            '5.9': '@dmtype != \'\'',
            '5.10': 'every $child in ./dm-mapping:INSTANCE satisfies  (not($child/@dmrole) or $child/@dmrole = \'\')',
            '5.11': 'every $child in ./dm-mapping:INSTANCE satisfies  (not($child/@dmrole) or $child/@dmrole = \'\')',
            '5.12': 'VALID',
            '5.13': 'VALID',
            '5.14': 'VALID',
            '5.15': 'VALID',
            '5.16': 'if (@dmid) then ( @dmid != \'\')',
            '5.17': 'missing required attribute \'dmtype\'',
            '5.18': '@dmtype != \'\'',
            '5.20': 'count (dm-mapping:INSTANCE[@dmrole != \'\']) eq 0',
            '5.21': 'count (dm-mapping:INSTANCE[@dmrole != \'\']) eq 0',
            '5.22': 'VALID',
            '5.23': 'VALID',
            '5.24': 'VALID',
            '5.25': 'VALID',
            '5.26': 'if (@dmid) then ( @dmid != \'\')',
            '5.27': 'missing required attribute \'dmtype\'',
            '5.28': '@dmtype != \'\'',
            '5.29': 'count($grandchild/dm-mapping:PRIMARY_KEY) gt 0 )',
            '5.30': 'count (dm-mapping:INSTANCE[@dmrole != \'\']) eq 0',
            '5.31': 'count (dm-mapping:INSTANCE[@dmrole != \'\']) eq 0',
            '5.32': 'VALID',
            '5.33': 'VALID',
            '5.34': 'VALID',
            '5.35': 'VALID',
            '5.36': 'if (@dmid) then ( @dmid != \'\')',
            '5.37': 'missing required attribute \'dmtype\'',
            '5.38': '@dmtype != \'\'',
            '5.40': 'VALID',
            '5.41': 'VALID',
            '5.42': 'every $child in ./dm-mapping:INSTANCE satisfies  $child/@dmrole != \'\'',
            '5.43': 'every $child in ./dm-mapping:INSTANCE satisfies  $child/@dmrole != \'\'',
            '5.44': 'every $child in ./dm-mapping:INSTANCE satisfies  $child/@dmrole != \'\'',
            '5.45': 'every $child in ./dm-mapping:INSTANCE satisfies  $child/@dmrole != \'\'',
            '5.46': 'if (@dmid) then ( @dmid != \'\')',
            '5.47': 'missing required attribute \'dmtype\'',
            '5.48': '@dmtype != \'\'',
            '5.50': 'VALID',
            '5.51': 'VALID',
            '5.52': 'VALID',
            '5.53': 'VALID',
            '5.54': 'VALID',
            '5.55': 'VALID',
            '5.56': 'VALID',
            '5.57': 'Unexpected child with tag \'dm-mapping:PRIMARY_KEY\' at position 2.',
            '5.58': 'VALID',
            '5.59': 'Unexpected child with tag \'dm-mapping:OTHER\' at position 3.',
            }

class Test(unittest.TestCase):

    def testOK(self):
        self.assertTrue(TestRunner.regarde_si_OK(mapping_sample, "test_5"), "file should be valid")

    def testKO(self):
        self.assertTrue(TestRunner.regarde_si_KO(mapping_sample, "test_5", expected), "invalid file test failed.")


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
