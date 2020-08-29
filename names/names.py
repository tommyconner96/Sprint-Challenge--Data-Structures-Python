import time
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# this is the original solution and it is O(n^2) because of the nested for loops
# # Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# defining bst_node, setting the root as names_1 so we can loop through it
bst_node = BSTNode(names_1[0])

# adding all the names to thew BST
for name in names_1:
    bst_node.insert(name)
for name in names_2:
    # if there are duplicates append them
    if bst_node.contains(name):
        duplicates.append(name)

end_time = time.time()
# around .1 seconds on my laptop!
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# alternate solution for stretch goal:
# this is actually significantly faster! around 0.0025 seconds!!
# same = set(names_1).intersection(names_2)

# for line in same:
#     duplicates.append(line)
