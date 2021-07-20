# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

a_n_1 = 1
a_n = 2
a_nx1 = a_n_1 + a_n
s = a_n

while a_nx1 <= 4e6:
    if a_nx1 % 2:
        s += a_nx1
    a_n_1 = a_n
    a_n = a_nx1
    a_nx1 = a_n_1 + a_n

print(s)