# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
#
# 3
# 7 4
# 2 4 6
# 8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom of the triangle below:
#
# NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)


rawdata = [[int(el) for el in level.split(' ')] for level in
"""75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23""".split("\n")]

print(rawdata)

# Duplicate inner element
data = []
for r, row in enumerate(rawdata):
    new_row = []
    if r > 0:
        for e, el in enumerate(row):
            if (e > 0) and (e < r):
                new_row += [el, el]
            else:
                new_row += [el]
    else:
        new_row = row
    print(new_row)
    data += new_row

#print(data)

from binarytree import build
root = build(data)
print(root)

# Recursive function
def printPath(node, leaf_node):

    # base case
    if (node == None):
        return False

    # return True if this node is the target_leaf
    # or target leaf is present in one of its
    # descendants
    if (node == leaf_node or
            printPath(node.left, leaf_node) or
            printPath(node.right, leaf_node)) :
        print(node.value, end = " ")
        return True

    return False

# Recursive function
def max_path_sum(node, current_sum):

    global max_sum
    global leaf_node

    if node == None:
        return

    current_sum += node.value

    if node.left == None and node.right == None:
        if current_sum > max_sum:
            max_sum = current_sum
            leaf_node = node
            print(node.value)

    max_path_sum(node.left, current_sum)
    max_path_sum(node.right, current_sum)

max_sum = 0
leaf_node = None
max_path_sum(root, current_sum=0)
printPath(root, leaf_node)
#print(leaf_node, max_sum)