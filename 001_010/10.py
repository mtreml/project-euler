# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

N = 2000000
not_primes = [0]*N
num = 3
s = 2
while num < N:
    if not_primes[num] == 0:
        s += num
        i = num
        # Mark multiples of num since the cannot be prime
        while i < N:
            not_primes[i] = 1
            i += num
    num += 2

print(s)