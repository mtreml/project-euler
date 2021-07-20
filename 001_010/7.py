# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?


def is_prime(num):
    i = 2
    while i**2 <= num:
        if num % i == 0:
            return False
        i += 1
    return True

def nth_prime_naive(n):
    if n <= 0:
        return ValueError
    if n == 1:
        return 2
    count = 1
    num = 1
    while count < n:
        num += 2 # speedup
        if is_prime(num):
            count += 1
    return num

def nth_prime(n):
    """
    Sieve of erastothenes
    """
    return num

n = 10001
print(nth_prime_naive(n))
