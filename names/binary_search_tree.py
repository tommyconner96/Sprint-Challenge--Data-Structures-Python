"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Compare target value to node.value
        # If value > node.value:
        if value >= self.value:
            # Go right
            # If node.right is None:
            if self.right is None:
                # Create the new node there
                self.right = BSTNode(value)
            else:  # self.right is a BSTNode
                # Do the same thing (aka recurse)
                # Insert value into node.right
                # right_child is a BSTNode, so we can call insert on it
                right_child = self.right
                right_child.insert(value)
        # Else if value < node.value
        if value < self.value:
            # Go Left
            # If node.left is None:
            if self.left is None:
                # Create node
                self.left = BSTNode(value)
            else:
                # Do the same thing
                # (compare, go left or right)
                # Insert value into node.left
                left_child = self.left
                left_child.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if targett = value
        if target == self.value:
            return True
        # if target > value go right (unless it is none)
        elif target > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        # if target < value go left (unless none)
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        return False

    # Return the maximum value found in the tree
    def get_max(self):
        # the node with the maximum value will also be the right-most node
        if self.right is None:
            # Base Case
            # We're already at the right most node
            return self.value
        else:
            # Recursive case: make the problem smaller to get to the base case
            # Go right
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # Will have to look at both branches
        # Start at the root
        fn(self.value)
        if self.left is not None:
            # Go left
            self.left.for_each(fn)
        if self.right is not None:
            # Go right
            self.right.for_each(fn)


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass
 # psuedo code from class for bredth_first_traversal
# def breadth_first_traversal(self, fn):
#         pass
#         # Start at the root
#         # Push it onto the queue
#         #
#         # While queue is not empty:
#         # Cur_node = Remove from the queue
#         # Add cur_node children to the queue
#         # Process cur_node
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  
