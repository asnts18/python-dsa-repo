"""
    Abegail Santos
    Date: 11/13/24
"""

def is_valid(s):
    """
    A function to check if input string contains 
    valid parenthesization.
    Every opening parenthesis should be closed by the same kind of parenthesis
    and this must be in the correct order 
    """
    
    # initialize hashmap and stack 
    hashmap = {"}":"{", "]":"[", ")":"("} # contains correct pairs 
    stack = [] # should keep opening brackets
    
    for char in s:
    # if char is an opening bracket, append it to stack
        if char in hashmap.values():
            stack.append(char)
            
    # if char is a closing bracket, check against top element of stack
        else:
            if stack:
                popped_element = stack.pop() # pops element and assigns it to var
            else:
                popped_element = "*" # dummy value 
            
            if popped_element != hashmap[char]:
                return False
            
    return not stack # return True if stack is empty. 


def main():
    s1 = "{[()]}" # should be True
    s2 = "{()]}" # should be False
    s3 = "" # should be True
    s4 = "{()]}}}" # should be False
    
    print(is_valid(s1)) 
    print(is_valid(s2)) 
    print(is_valid(s3)) 
    print(is_valid(s4))



if __name__ == "__main__":
    main()
