'''
Created on 3 Jan 2018

@author: wbartlett
'''
import unittest
import main


class Test(unittest.TestCase):


    def testCompiles(self):
        main.api


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()