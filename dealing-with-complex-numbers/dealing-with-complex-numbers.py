"""Classes: Dealing with Complex Numbers.

For this challenge, you are given two complex numbers, and you have to print
the result of their addition, subtraction, multiplication, division and modulus
operations.

The real and imaginary precision part should be correct up to two decimal
places.

Input Format

One line of input: The real and imaginary part of a number separated by a
space.

Output Format

For two complex numbers C and D, the output should be in the following sequence
on separate lines:

C + D
C - D
C * D
C / D
mod(C)
mod(D)

For complex numbers with non-zero real and complex part, the output should be
in the following format:

A + Bi

Replace the plus symbol + with a minus symbol - when B < 0.

For complex numbers with a zero complex part i.e. real numbers, the output
should be:

A + 0.00i

For complex numbers where the real part is zero and the complex part is
non-zero, the output should be:

0.00 + Bi

Sample Input

2 1
5 6

Sample Output

7.00+7.00i
-3.00-5.00i
4.00+17.00i
0.26-0.11i
2.24+0.00i
7.81+0.00i

Concept

Python is a fully object-oriented language like C++, Java, etc.

Methods with a double underscore before and after their name are considered as
built-in methods. They are used by interpreters and are generally used in the
implementation of overloaded operators or other built-in functionality.

__add__-> Can be overloaded for + operation

__sub__ -> Can be overloaded for - operation

__mul__ -> Can be overloaded for * operation
"""
import math


class Complex(object):
    """An implementation of complex numbers."""

    def __init__(self, real, imaginary):
        """Initialize the Complex object with real and imaginary arguments."""
        self.real = float(real)
        self.imaginary = float(imaginary)

    def __add__(self, no):
        """Return a new Complex object with the result of addition."""
        real = self.real + no.real
        imaginary = self.imaginary + no.imaginary

        return Complex(real, imaginary)

    def __sub__(self, no):
        """Return a new Complex object with the result of subtraction."""
        real = self.real - no.real
        imaginary = self.imaginary - no.imaginary

        return Complex(real, imaginary)

    def __mul__(self, no):
        """Return a new Complex object with the result of multiplication."""
        real = ((self.real * no.real)
                + (-1 * self.imaginary * no.imaginary))
        imaginary = ((self.real * no.imaginary)
                     + (self.imaginary * no.real))

        return Complex(real, imaginary)

    def __truediv__(self, no):
        """Return a new Complex object with the result of division."""
        conjugate = Complex(no.real, -1 * no.imaginary)
        numerator = Complex(self.real, self.imaginary) * conjugate
        denominator = no * conjugate
        real = numerator.real / denominator.real
        imaginary = numerator.imaginary / denominator.real

        return Complex(real, imaginary)

    def mod(self):
        """Return a new Complex object with the result of modulus operation."""
        real = math.sqrt(self.real**2 + self.imaginary**2)
        imaginary = 0.0

        return Complex(real, imaginary)

    def __str__(self):
        """Return a string representation of the Complex object."""
        if self.imaginary == 0:
            result = f'{self.real:.2} + 0.00i'

        elif self.real == 0:

            if self.imaginary >= 0:
                result = f'0.00+{self.imaginary:.2f}i'

            else:
                result = f'0.00-{self.imaginary:.2f}i'

        elif self.imaginary > 0:
            result = f'{self.real:.2f}+{self.imaginary:.2f}i'

        else:
            result = f'{self.real:.2f}-{abs(self.imaginary):.2f}i'

        return result


def main():
    """Run the test."""
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep='\n')


if __name__ == '__main__':
    main()
