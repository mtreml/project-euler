# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

N = 20
dividers = range(1, N+1)

N = 0

searching = True
while searching:
    N += 1
    for d in dividers:
        if N % d != 0:
            searching = True
            break
        else:
            searching = False

print(N)