# Homework 01: Classifying Triangles
# Author: Gabrielle McCormack
# Date Completed: 09.02.2018
# Pledge: "I pledge my honor that I have abided by the Stevens Honor System." - Gabrielle McCormack

import math

def classify_triangle(a, b, c):
    # check if positive number
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except (ValueError, TypeError):
        tri = 'Invalid number. Not a triangle.'
        return tri

    if (a <= 0 or b <= 0 or c <= 0):
        tri = 'Invalid number. Not a triangle.'
        return tri

    # check if triangle is scalene
    if (a != b and b != c and a != c):
        # check if triangle is right
        if (round((math.pow(a, 2) + math.pow(b, 2)),2) == round(math.pow(c, 2),1)):
            tri = 'Triangle is scalene and right.'
            return tri
        else:
            tri = 'Triangle is scalene.'
            return tri
    # check if triangle is isoceles
    elif (((a == b) and (a != c)) or ((b == c) and (a != c)) or ((a == c) and (a != b))) :
        # check if triangle is right
        if (round((math.pow(a, 2) + math.pow(b, 2)),2) == round(math.pow(c, 2),1)):
            tri = 'Triangle is isosceles and right.'
            return tri
        else:
            tri = 'Triangle is isosceles.'
            return tri
    else:
        tri = 'Triangle is equilateral.'
        return tri



