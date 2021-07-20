# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

n1 = 100
n2 = 100

N = n1 * n2

palindroms = []
highest = 0

def is_palindromic(N):
    s = str(N)
    if len(s) % 2 == 0:
        if s[:len(s)//2] == s[len(s)//2::][::-1]:
            return True
        else:
            return False
    else:
        return False

#print(is_palindromic(441144))

for n1 in range(100, 999):
    for n2 in range(100, 999):
        w = n1 * n2
        print(n1, n2, w)
        if is_palindromic(w):
            palindroms.append(w)
        n2 += 1
    n1 += 1

print(palindroms)
print(max(palindroms))

