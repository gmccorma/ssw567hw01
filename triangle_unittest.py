# Homework 01: Classifying Triangles
# Author: Gabrielle McCormack
# Date Completed: 09.02.2018
# Pledge: "I pledge my honor that I have abided by the Stevens Honor System." - Gabrielle McCormack

import unittest
import math
from triangle import classify_triangle


class MyTestCase(unittest.TestCase):

    def test_equilateral1(self):
        self.assertEqual(classify_triangle(1,1,1), 'Triangle is equilateral.')

    def test_equilateral2(self):
        self.assertEqual(classify_triangle('a', 1, 1), 'Invalid number. Not a triangle.')

    def test_equilateral3(self):
        self.assertEqual(classify_triangle(-9, 1, 1), 'Invalid number. Not a triangle.')

    def test_isosceles1(self):
        self.assertEqual(classify_triangle(3,3,6), 'Triangle is isosceles.')

    def test_isosceles2(self):
        self.assertEqual(classify_triangle('a','b',10), 'Invalid number. Not a triangle.')

    def test_isosceles3(self):
        self.assertEqual(classify_triangle(10,-3,10), 'Invalid number. Not a triangle.')

    def test_isosceles4(self):
        self.assertEqual(classify_triangle(1,1,math.sqrt(2)), 'Triangle is isosceles and right.')

    def test_scalene1(self):
        self.assertEqual(classify_triangle(1,5,8), 'Triangle is scalene.')

    def test_scalene2(self):
        self.assertEqual(classify_triangle('a',4,10), 'Invalid number. Not a triangle.')

    def test_scalene3(self):
        self.assertEqual(classify_triangle(3,4,5), 'Triangle is scalene and right.')

    def test_scalene4(self):
        self.assertEqual(classify_triangle(-1,0,10), 'Invalid number. Not a triangle.')


if __name__ == '__main__':
    unittest.main()
