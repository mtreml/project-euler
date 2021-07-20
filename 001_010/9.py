#
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#     a2 + b2 = c2
#
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


from math import sqrt

def C(a, b):

    return sqrt(a**2 + b**2)


def B(a):

    return (2000*a - 1000000) / (2*a - 2000)


def is_pythagorean(a, b, c):
    if a < 0 or b < 0 or c < 0:
        return False
    if a % 1 != 0 or b % 1 != 0 or c % 1 != 0:
        return False
    if not (a < b < c):
        return False
    else:
        if a**2 + b**2 == c**2:
            return True
        else:
            return False

product = 0
for a in range(1000):
    b = B(a)
    c = C(a, b)
    product = a*b*c
    if is_pythagorean(a, b, c):
        break

print(product)