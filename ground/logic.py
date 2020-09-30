# -*- coding: utf-8 -*-
from common import isNotZero, print_method


class SampleClass:
    def __init__(self, hoge, fuga, height, width):
        self.hoge = hoge
        self.fuga = fuga
        self.height = height
        self.width = width

    def print_hoge(self):
        print_method(self.hoge)

    def print_fuga(self):
        print_method(self.fuga)

    def print_hoge_and_fuga(self):
        print_method(self.hoge, self.fuga)

    def square_area(self):
        if isNotZero(self.height) and isNotZero(self.width):
            return self.height * self.width


if __name__ == "__main__":
    sampleClass = SampleClass('hoge', 'fuga', 2, 4)
    sampleClass.print_hoge()
    sampleClass.print_fuga()
    sampleClass.print_hoge_and_fuga()
    print_method(sampleClass.square_area())
