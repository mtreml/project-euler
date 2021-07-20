# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#     13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.


def next_collatz_number(n):
    if n % 2 == 0:
        return int(n/2)
    else:
        return (3*n+1)

longest_chain_length = 0
n0_longest = 0
for n0 in range(2, 1000000):
    chain = [n0]
    while chain[-1] != 1:
        chain.append(next_collatz_number(chain[-1]))
    if len(chain) > longest_chain_length:
        longest_chain_length = len(chain)
        n0_longest = n0
print(n0_longest)
