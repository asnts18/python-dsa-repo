from typing import List
from queue import Queue
from TreeNode import *

class BinaryTree:
    def __init__(self, nodes):
        self.root = self.createBinaryTree(nodes)
        
    def createBinaryTree(self, nodes):
        if len(nodes) == 0:
            return None
        
        # create root node of binary tree
        root = TreeNode(nodes[0].data)
        
        #create queue and add root node to it
        queue = Queue()
        queue.put(root)
        
        # iterate over list of nodes starting from second node 
        i = 1
        while i < len(nodes):
            # get next node from queue
            curr = queue.get()  
                
            # if node is not empty, create new TreeNode object for its left child
            # set left child as current node, and add to queue
            if nodes[i] is not None:
                curr.left = TreeNode(nodes[i].data)
                queue.put(curr.left)
                
            i += 1
            
            # if there are more nodes in the list and the next node is not None
            # create a new TreeNode obejct for right child and set it as right child
            # of current node, and add to queue. 
            if i < len(nodes) and nodes[i] is not None:
                curr.right = TreeNode(nodes[i].data)
                queue.put(curr.right)
                
            i += 1
            
        return root