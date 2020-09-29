# -*- coding: utf-8 -*-
from common import print_method


class SampleClass:
    def __init__(self, hoge, fuga):
        self.hoge = hoge
        self.fuga = fuga

    def print_hoge(self):
        print_method(self.hoge)

    def print_fuga(self):
        print_method(self.fuga)

    def print_hoge_and_fuga(self):
        print_method(self.hoge, self.fuga)


if __name__ == "__main__":
    sampleClass = SampleClass('hoge', 'fuga')
    sampleClass.print_hoge()
    sampleClass.print_fuga()
    sampleClass.print_hoge_and_fuga()
