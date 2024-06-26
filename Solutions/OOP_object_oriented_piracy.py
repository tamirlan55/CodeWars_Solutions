# https://www.codewars.com/kata/search/my-languages?q=&tags=Object-oriented%20Programming&xids=completed&beta=false&order_by=popularity%20desc

'''Ahoy matey!

You are a leader of a small pirate crew. And you have a plan. With the help of 
OOP you wish to make a pretty efficient system to identify ships with heavy booty on board!

Unfortunately for you, people weigh a lot these days, 
so how do you know if a ship is full of gold and not people?

You begin with writing a generic Ship class / struct:

class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
Every time your spies see a new ship enter the dock, 
they will create a new ship object based on their observations:

draft - an estimate of the ship's weight based on how low it is in the water
crew - the count of crew on board
Titanic = Ship(15, 10)
Task
You have access to the ship "draft" and "crew". "Draft" is the total 
ship weight and "crew" is the number of humans on the ship.

Each crew member adds 1.5 units to the ship draft. If after removing the weight of the crew, 
the draft is still more than 20, then the ship is worth looting. 
Any ship weighing that much must have a lot of booty!

Add the method

is_worth_it
to decide if the ship is worthy to loot. For example:

Titanic.is_worth_it()
False
'''

import pytest

class Ship:
    '''Класс корабль'''
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew

    def is_worth_it(self):
        '''Функция оценивающая стоит ли грабить корабль'''
        if (self.draft - 1.5 * self.crew) > 20:
            return True
        else:
            return False


@pytest.mark.parametrize(
    'obj, decision',
    [
        (Ship(30, 10), False),
        (Ship(100, 5), True),
        (Ship(10, 5), False),
        (Ship(45, 30), False),
        (Ship(40, 10), True)
    ]
)
def test_is_worth_it(obj, decision):
    '''Функция тестирования класса'''
    assert obj.is_worth_it() == decision
