# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#
# How many such routes are there through a 20×20 grid?

from scipy.special import comb

# The number of NE-lattice paths from (0,0) -> (n, k) is given by the Binomial coefficient (n+k k).

n = 20
print(comb(n+n, n, exact=True))
