#https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python

'''This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.'''

import pytest

def accum(st: str):
    '''Функция умножающая букву на индекс'''
    arr = []
    for index, letter in enumerate(st):
        elem = letter * (index + 1)
        arr.append(elem[0].upper() + elem[1::].lower())

    return '-'.join(arr)



class TestAccum():
    '''Класс для тестирования функции'''

    @pytest.mark.parametrize(
        'x, res',
        [
            ('ABT', 'A-Bb-Ttt'),
            ('akCe', 'A-Kk-Ccc-Eeee'),
            ('NgqL', 'N-Gg-Qqq-Llll')
        ]
    )
    def test_accum(self, x: str, res):
        '''Функция тестирования'''
        assert accum(x) == res
