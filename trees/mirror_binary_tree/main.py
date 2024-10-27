"""
    Abegail Santos
    Code sample from Educative 
"""

from BinaryTree import *
from TreeNode import *
from collections import deque

# global variables to support step-by-step printing
change = 0
master_root = None

def mirror_binary_tree(root):
    global change, master_root
    
    # base case: empty tree
    if not root: 
        return None 
    
    # post order traversal 
    if root.left:
        mirror_binary_tree(root.left)
    if root.right:
        mirror_binary_tree(root.right)
    
    # swap
    root.left, root.right = root.right, root.left
    
    # print 
    if master_root and (root.left or root.right):
        change += 1
        print("\n\tChange ", change, ", at node ",
              root.data, ":", sep="")
        display_tree(master_root)
    
    return root

def display_tree(root, level=0, prefix="Root: "):
    """
    Recursively displays the binary tree structure with indentation for each level.
    """
    
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.data))  # Indentation increases with depth
        if root.left or root.right:  # Display left and right branches if they exist
            if root.left:
                display_tree(root.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
            if root.right:
                display_tree(root.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")
    else:
        print("Tree is empty.")

def main():
    global change, master_root
    
    input_trees = [
        [TreeNode(100), TreeNode(50), TreeNode(200), TreeNode(25), TreeNode(75), TreeNode(125), TreeNode(350)],
        [TreeNode(100), TreeNode(50), TreeNode(200), TreeNode(25), TreeNode(110), TreeNode(125), TreeNode(350)],
        [TreeNode(100), TreeNode(50), TreeNode(200), TreeNode(25), TreeNode(75), TreeNode(90), TreeNode(350)],
        [TreeNode(25), TreeNode(50), TreeNode(75), TreeNode(100), TreeNode(125), TreeNode(350)],
        [TreeNode(350), TreeNode(125), TreeNode(100), TreeNode(75), TreeNode(50), TreeNode(25)],
        [TreeNode(100)],
        [TreeNode(1), TreeNode(2), None, TreeNode(3), None, TreeNode(4)],
        [TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), None, None, TreeNode(5)],
        []
    ]

    indx = 1
    for i in input_trees:
        tree = BinaryTree(i)

        print(indx, ".\tBinary Tree:", sep="")
        indx += 1
        display_tree(tree.root)
        change = 0
        master_root = tree.root
        mirror_binary_tree(tree.root)
        print("\n\tMirrored binary tree:")
        display_tree(tree.root)
        print("-"*100)


    
if __name__ == '__main__':
    main()