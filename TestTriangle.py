# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    # Right triangle tests
    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(5,12,13),'Right','5,12,13 is a Right triangle')

    # Equilateral triangle tests
    def testEquilateralA(self):
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testEquilateralB(self):
        self.assertEqual(classifyTriangle(10,10,10),'Equilateral','10,10,10 should be equilateral')

    def testEquilateralC(self):
        self.assertEqual(classifyTriangle(100,100,100),'Equilateral','100,100,100 should be equilateral')

    # Isosceles triangle tests
    def testIsoscelesA(self):
        self.assertEqual(classifyTriangle(2,2,3),'Isoceles','2,2,3 should be Isoceles')

    def testIsoscelesB(self):
        self.assertEqual(classifyTriangle(3,2,2),'Isoceles','3,2,2 should be Isoceles')

    def testIsoscelesC(self):
        self.assertEqual(classifyTriangle(2,3,2),'Isoceles','2,3,2 should be Isoceles')

    # Scalene triangle tests
    def testScaleneA(self):
        self.assertEqual(classifyTriangle(3,4,6),'Scalene','3,4,6 should be Scalene')

    def testScaleneB(self):
        self.assertEqual(classifyTriangle(7,8,9),'Scalene','7,8,9 should be Scalene')

    def testScaleneC(self):
        self.assertEqual(classifyTriangle(10,11,12),'Scalene','10,11,12 should be Scalene')

    # NotATriangle tests
    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(1,2,3),'NotATriangle','1,2,3 is NotATriangle')

    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle(1,1,10),'NotATriangle','1,1,10 is NotATriangle')

    def testNotATriangleC(self):
        self.assertEqual(classifyTriangle(10,1,1),'NotATriangle','10,1,1 is NotATriangle')

    # InvalidInput tests
    def testInvalidInputNeg(self):
        self.assertEqual(classifyTriangle(-1,1,1),'InvalidInput','-1,1,1 should be InvalidInput')

    def testInvalidInputZero(self):
        self.assertEqual(classifyTriangle(0,1,1),'InvalidInput','0,1,1 should be InvalidInput')

    def testInvalidInputOver(self):
        self.assertEqual(classifyTriangle(201,1,1),'InvalidInput','201,1,1 should be InvalidInput')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
