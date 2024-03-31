# https://www.codewars.com/kata/55c1d030da313ed05100005d/train/python

'''Now that we have a Block let's move on to something slightly more complex: a Sphere.

Arguments for the constructor
radius -> integer or float (do not round it)
mass -> integer or float (do not round it)
Methods to be defined
get_radius()       =>  radius of the Sphere (do not round it)
get_mass()         =>  mass of the Sphere (do not round it)
get_volume()       =>  volume of the Sphere (rounded to 5 place after the decimal)
get_surface_area() =>  surface area of the Sphere (rounded to 5 place after the decimal)
get_density()      =>  density of the Sphere (rounded to 5 place after the decimal)
Example
ball = Sphere(2,50)
ball.get_radius() ->       2
ball.get_mass() ->         50
ball.get_volume() ->       33.51032
ball.get_surface_area() -> 50.26548
ball.get_density() ->      1.49208
Any feedback would be much appreciated
'''
import math
import pytest


class Sphere(object):
    '''Класс сфера'''
    def __init__(self, radius: int, mass: int):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        '''Функция возвращающая радиус'''
        return self.radius

    def get_mass(self):
        '''Function, which returned mass'''
        return self.mass

    def get_volume(self):
        '''Function, which returned volume'''
        return (4 / 3) * math.pi * (self.radius) ** 3

    def get_surface_area(self):
        '''Function, which returned the surface area'''
        return 4 * math.pi * (self.radius ** 2)

    def get_density(self):
        '''Function, which returned the density of ball'''
        return self.get_mass() / self.get_volume()


@pytest.mark.parametrize(
    'obj, res',
    [
        (Sphere(2, 50), 33.51032)
    ]
)
def test_get_volume(obj, res):
    '''Test function'''
    assert obj.get_volume() == res
