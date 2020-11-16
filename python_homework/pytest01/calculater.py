# -*- coding: utf-8 -*-
# @author: Kennnycyq
# @time: 2020/11/16 9:56 PM


class Calculator:

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print("除数不可为0!")
            return False