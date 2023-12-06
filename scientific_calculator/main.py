import math

class Scientific_calculator:
    """
    This class represents a scientific calculator with various mathematical functions.

    Methods:
        add(*args): Returns the sum of the input arguments.
        sub(*args): Returns the difference between the first argument and the rest of the arguments.
        div(a, b): Returns the quotient of a divided by b.
        mult(*args): Returns the product of the input arguments.
        mult2(*args): Returns the product of the input arguments using the math.prod() function.
        remainder(a, b): Returns the remainder of a divided by b.
        square_root(a): Returns the square root of a.
        power(a, b): Returns a raised to the power of b.
        factorial(a): Returns the factorial of a.
        sine(a): Returns the sine of a.
        cosine(a): Returns the cosine of a.
        tangent(a): Returns the tangent of a.
        rad_deg(a): Converts radians to degrees.
        deg_rad(a): Converts degrees to radians.
    """
    def add(self, *args):
        return sum(args)

    def sub(self, *args):
        subtract = args[0]
        for i in range(1, len(args)):
            subtract -= args[i]
        return subtract

    def div(self, a, b):
        try:
            return a / b
        except ZeroDivisionError as e:
            print(e)

    def mult(self, *args):
        multi = 1
        for i in args:
            multi *= i
        return multi

    def mult2(self, *args):
        return math.prod(args)

    def remainder(self, a, b):
        return a % b

    def square_root(self, a):
        return a ** 0.5

    def power(self, a, b):
        return a ** b

    def factorial(self, a):
        try:
            return math.factorial(a)
        except TypeError:
            print("Number must be positive integer!")
        except ValueError:
            print("Number must be positive integer!")

    def sine(self, a):
        return math.sin(a)

    def cosine(self, a):
        return math.cos(a)

    def tangent(self, a):
        return math.tan(a) if round(self.deg_rad(a), 15) != round(self.deg_rad(90), 15) else math.inf

    def rad_deg(self, a):
        return math.degrees(a)

    def deg_rad(self, a):
        return math.radians(a)
    

def main():
    calc = Scientific_calculator()

    calc.add(5, 2)

    calc.sub(5, -2)

    calc.div(2, 9)

    calc.mult(5, 0.5)

    calc.remainder(7, 5)

    calc.square_root(8)

    calc.factorial(7)

    calc.sine(calc.deg_rad(13))

    calc.cosine(calc.deg_rad(13))

    calc.tangent(calc.deg_rad(90))

    calc.deg_rad(19)

    calc.rad_deg(19)


if __name__ == "__main__":
    main()
