#https://www.codewars.com/kata/55a710b462afc49a540000b9/train/python

'''7 Kyu
Correct this code so that it takes one argument, x, and returns "x is more than zero" 
if x is positive (and nonzero), and otherwise, returns "x is equal to or less than zero." 
In both cases, replace x with the actual value of x.
'''

import random
import pytest


def corrections(x: int):
    '''Функция сравнения Х с нулем'''
    if x > 0:
        return f'{x} is more than zero.'
    return f'{x} is equal to or less than zero.'


class TestCW:
    '''БЛОК ТЕСТИРОВАНИЯ'''
    def test_positive_value(self):
        '''Тестирование положительных чисел'''
        for x in range(10):
            x = random.randrange(1, 250, 1)
            assert corrections(x) == f'{x} is more than zero.'

    def test_negative_value(self):
        '''Тестирование отрицательных и равных нулю'''
        for x in range(15):
            x = random.randrange(-250, 1, 1)
            assert corrections(x) == f'{x} is equal to or less than zero.'
