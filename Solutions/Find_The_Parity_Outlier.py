# https://www.codewars.com/kata/5526fc09a1bbd946250002dc/train/python
'''6kyu'''
'''You are given an array (which will have a length of at least 3, b
ut could be very large) containing integers. The array is either entirely 
comprised of odd integers or entirely comprised of even integers except for 
a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36] -->  11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21] --> 160 (the only even number)
'''

import pytest

def find_outlier(integers: list):
    '''Функция поиска выброса'''
    arr_temp_odd = []
    arr_temp_even = []
    for elem in integers:
        if elem % 2 == 0:
            arr_temp_even.append(elem)
        elif elem % 2 != 0:
            arr_temp_odd.append(elem)
        if (len(arr_temp_even) > 1 and len(arr_temp_odd) == 1) or (len(arr_temp_odd) > 1 and len(arr_temp_even) == 1):
            break
    if len(arr_temp_odd) == 1:
        return arr_temp_odd[0]
    else:
        return arr_temp_even[0]


class TestFindOutlier():
    '''Класс для тестирования'''
    @pytest.mark.parametrize(
        'inp_list, res',
        [
            ([2, 4, 0, 100, 4, 11, 2602, 36], 11),
            ([160, 3, 1719, 19, 11, 13, -21], 160)
        ]
    )
    def test_find_outlier(self, inp_list: list, res: int):
        '''Функция тестирования'''
        assert find_outlier(inp_list) == res

