from jsbmath import add
from jsbmath import substract
from jsbmath.extras import multiply
from jsbmath.extras import divide
from jsbmath import teacher


if __name__ == "__main__":

    print("Testing started...")

    assert(add.add(2,2) == 4)
    
    assert(substract.substract(5,2) == 3)

    assert(multiply.multiply(2,2) == 4)

    assert(divide.divide(6,2) == 3)

    #with teacher
    t = teacher.teacher()

    assert(t.addition(2,2) == 4)
    
    assert(t.substraction(5,2) == 3)

    assert(t.multiplication(2,2) == 4)

    assert(t.division(6,2) == 3)

    print("Testing finished...")
