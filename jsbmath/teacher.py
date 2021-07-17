from singleton3 import Singleton

from . import add
from . import substract
from .extras import multiply
from .extras import divide

class teacher(metaclass=Singleton):

    def __init__(self):
        pass

    def addition(self, val1, val2):
        return add.add(val1,val2)

    def substraction(self, val1, val2):
        return substract.substract(val1, val2)

    def multiplication(self, val1, val2):
        return multiply.multiply(val1, val2)

    def division(self, val1, val2):
        return divide.divide(val1, val2)


