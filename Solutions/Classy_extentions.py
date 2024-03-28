# https://www.codewars.com/kata/55a14aa4817efe41c20000bc/train/python

'''Classy Extensions
Classy Extensions, this kata is mainly aimed at the new JS ES6 Update 
introducing extends keyword. You will be preloaded with the Animal class, 
so you should only edit the Cat class.
Task
Your task is to complete the Cat class which Extends Animal and replace the 
speak method to return the cats name + meows. e.g. 'Mr Whiskers meows.'
The name attribute is passed with this.name (JS), @name (Ruby) or self.name (Python).
'''
import pytest

class Animal:
    '''Родительский класс'''
    pass


class Cat(Animal):
    '''Класс кот'''
    def __init__(self, name: str):
        self.name = name

    def speak(self):
        '''Метод'''
        return f'{self.name} meows.'

@pytest.mark.parametrize(
    'name, res',
    [
        ('Bob', 'Bob meows.'),
        ('Tom', 'Tom meows.'),
        ('Fred', 'Fred meows.')
    ]
)
def test_speak(name, res):
    '''Функция тестирования'''
    assert Cat(name).speak() == res
