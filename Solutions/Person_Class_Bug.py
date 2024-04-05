# https://www.codewars.com/kata/513f887e484edf3eb3000001/train/python

'''The following code was thought to be working properly, 
however when the code tries to access the age of the person instance it fails.

person = Person('Yukihiro', 'Matsumoto', 47)
print(person.full_name)
print(person.age)
For this exercise you need to fix the code so that it works correctly.

Note: the order of the person's full name is first name and last name.

'''
import pytest

class Person():
    '''Класс Человек'''
    def __init__(self, first_name, last_name, age: int = 20):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.full_name = f'{self.first_name} {self.last_name}'


@pytest.mark.parametrize(
    'fn, ln, age, res',
    [
        ('Miller', 'John', 32, 32),
        ('Spark', 'Mattew', 33, 33),
        ('McGill', 'James', 34, 34)
    ]
)
def test_class(fn, ln, age, res):
    '''Функция тестирования'''
    assert Person(fn, ln, age).age == res
