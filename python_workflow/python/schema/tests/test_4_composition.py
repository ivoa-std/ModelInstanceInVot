'''
Created on 16 juin 2020

@author: laurentmichel
'''
import unittest
from schema.validator.test_runner import TestRunner

mapping_sample = "./mapping_sample"
 

class Test(unittest.TestCase):


    def testOK(self):
        self.assertTrue(TestRunner.testOK(mapping_sample, "test_4"), "file should be valid")

    def testKO(self):
        self.assertTrue(TestRunner.testKO(mapping_sample, "test_4"), "file shouldn't be valid")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()