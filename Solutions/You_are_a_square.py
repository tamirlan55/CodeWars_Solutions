#https://www.codewars.com/kata/54c27a33fb7da0db0100040e/train/python

'''A square of squares
You like building blocks. You especially like building blocks that are squares. 
And what you even like more, is to arrange them into a square of square building blocks!

However, sometimes, you can't arrange them into a square. Instead, 
you end up with an ordinary rectangle! Those blasted things! 
If you just had a way to know, whether you're currently working in vain… 
Wait! That's it! You just have to check if your number of building blocks is a perfect square.

Task
Given an integral number, determine if it's a square number:

In mathematics, a square number or perfect square is an integer that is the 
square of an integer; in other words, it is the product of some integer with itself.

The tests will always use some integral number, 
so don't worry about that in dynamic typed languages.

Examples
-1  =>  false
 0  =>  true
 3  =>  false
 4  =>  true
25  =>  true
26  =>  false
'''

import pytest

def is_square(n):
    '''Функция, проверяющая, является ли число квадратом'''
    if n < 0:
        return False
    elif (n ** 0.5) == int(n ** 0.5):
        return True
    else:
        return False
    

class TestIsSquare():
    '''Класс для тестирования'''    
    @pytest.mark.parametrize(
        'n, res',
        [
            (0, True),
            (25, True),
            (92, False),
            (-4, False),
            (49, True),
            (4, True),
            (9, True),
            (55, False),
            (6, False),
            (-12, False),
            (5, False)
        ]
    )
    def test_is_square(self, n: int, res):
        ''''Функция для тестирования'''
        assert is_square(n) == res
