# https://www.codewars.com/kata/526571aae218b8ee490006f4/train/python

'''Write a function that takes an integer as input, and returns the number of 
bits that are equal to one in the binary representation of that number. 
You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, 
so the function should return 5 in this case
'''

import pytest

def count_bits(n):
    '''Функция, переводящая число в двоичную форму, и считающая количество бит числа'''
    out_number = []
    x = n
    while True:
        out_number.append(x % 2)
        x = x // 2
        if x // 2 < 1:
            out_number.append(x % 2)
            break
    return sum(filter(lambda x: x == 1, out_number))

class TestCoutnBits():
    '''Класс для тестирования функции count_bits'''
    @pytest.mark.parametrize(
        'n, res',
        [
            (14, 3),
            (63, 6),
            (77, 4),
            (21, 3),
            (11, 3),
            (331, 5)
        ]
    )
    def test_count_bits(self, n, res):
        '''Функция тестирующая основноую функцию'''
        assert count_bits(n) == res
