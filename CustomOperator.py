import operator
from math import floor


def divisionWithRemainder(numerator, denominator):
    quotient: int = floor(operator.truediv(numerator, denominator))
    remainder = numerator % denominator
    if remainder != 0:
        return "{quo}R{rem}".format(quo=quotient, rem=remainder)
    return quotient
