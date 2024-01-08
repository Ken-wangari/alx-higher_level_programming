#!/usr/bin/python3
'''Module for rectangle class.'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''A subclass representing a recatngle.'''
    def ___init__(self, width, height):
        '''Constructor.'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
