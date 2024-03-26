#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 17:29:53 2024

@author: maritaolano
"""

# Assignment 06 
# Question 2: Geometric Shapes Calculation 

# base case 
class Shape:
    def area(self):
        return None

    def perimeter(self):
        return None

# derived classes circle, rectangle, triangle 
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    # individual operations to calculate the area and perimeter 
    def area(self):
        return 3.14159 * self.radius ** 2
    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    # individual operations to calculate the area and perimeter 
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    # individual operations to calculate the area and perimeter 
    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

def main():
    # list of shapes
    shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 4, 5)]
    
    # print area and perimeter of each shape
    for shape in shapes:
        print("Shape:")
        print("Area:", shape.area())
        print("Perimeter:", shape.perimeter())
        print()

main()

    