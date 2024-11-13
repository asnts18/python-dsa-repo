"""
    Abegail Santos
    Date: 11/13/24
"""

from linked_list import LinkedList

def reverse_linked_list(linked_list):
    """
    A function to reverse linked list.
    """
    prev = None 
    curr = linked_list.head
    
    while curr is not None:
        next_node = curr.next # move next pointer forward, to be used as an anchor
        curr.next = prev # reverse curr's next pointer
        prev = curr # use curr as an anchor to move prev pointer forward
        curr = next_node # move curr forward
        
    linked_list.head = prev # after iterating, prev will be pointing to the last node which will be the new head. 
    return linked_list.head
    
def main():
    
    # initialize linked list and append new nodes 
    my_linked_list = LinkedList(4)
    my_linked_list.append(3)
    my_linked_list.append(2)
    my_linked_list.append(1)
    
    reverse_linked_list(my_linked_list)
    my_linked_list.print_list()
    
    
if __name__ == "__main__":
    main()
