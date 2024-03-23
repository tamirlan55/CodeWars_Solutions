#https://www.codewars.com/kata/57e8f757085f7c7d6300009a/train/python

'''Finding your seat on a plane is never fun, particularly for a long haul flight... 
You arrive, realise again just how little leg room you get, and sort of climb 
into the seat covered in a pile of your own stuff.

To help confuse matters (although they claim in an effort to do the opposite) 
many airlines omit the letters 'I' and 'J' from their seat naming system.

The naming system consists of a number (in this case between 1-60) that denotes 
the section of the plane where the seat is (1-20 = front, 21-40 = middle, 40+ = back). 
This number is followed by a letter, A-K with the exclusions mentioned above.

Letters A-C denote seats on the left cluster, D-F the middle and G-K the right.

Given a seat number, your task is to return the seat location in the following format:
'2B' would return 'Front-Left'.
If the number is over 60, or the letter is not valid, return 'No Seat!!'.
'''

import pytest

def plane_seat(a: str):
    '''Функция преобразует номер места в его фактическое примерное расположение'''
    arr = []
    if a[-1] in 'ABC':
        arr.append('-Left')
    elif a[-1] in 'DEF':
        arr.append('-Middle')
    elif a[-1] in 'GHK':
        arr.append('-Right')
    else:
        return 'No Seat!!'
    
    if int(a[:-1:1]) <= 20:
        arr.append('Front')
    elif 20 < int(a[:-1:1]) <= 40:
        arr.append('Middle')
    elif 40 < int(a[:-1:1]) <= 60:
        arr.append('Back')
    else:
        return 'No Seat!!'

    return arr[1] + arr[0]


class TestCW():
    '''Класс, в котором описаны функции для тестов'''
    @pytest.mark.parametrize(
        "inp, out", 
        [
            ('2B', 'Front-Left'),
            ('15C', 'Front-Left'),
            ('55A', 'Back-Left'),
            ('12H', 'Front-Right'),
            ('31E', 'Middle-Middle'),
            ('35D', 'Middle-Middle'),
            ('48F', 'Back-Middle'),
            ('25A', 'Middle-Left')
        ]
    )
    def test_plane_seat(self, inp, out):
        '''Тестирование функции'''
        assert plane_seat(inp) == out
