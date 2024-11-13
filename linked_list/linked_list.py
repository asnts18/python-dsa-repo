"""
    Abegail Santos
    Date: 11/13/24
    Source: DSA in Python Udemy
"""

class Node():
    """
    This is a class for a LinkedList node 
    
    A linked list node contains:
    - value 
    - pointer to the next node
    """
    def __init__(self, value, next = None):
        self.value = value
        self.next = next


class LinkedList():
    """
    This is a class for a LinkedList 
    
    A linked list contains: nodes, head, tail
    """
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
