def is_palindrome(s):
    left = 0                    # starting index
    right = len(s) - 1          # last index, adjusted
    while left < right:         
        if s[left] != s[right]: # return false if a pair does not match
            return False
        left += 1               # increment left pointer
        right -= 1              # decrement right pointer
    return True

def main():
    test_cases = ["RACECAR", "ABBA", "HELLO"]
    
    for i in range(len(test_cases)):
        if is_palindrome(test_cases[i]):
            print(test_cases[i] + " is a palindrome.\n")
        else:
            print(test_cases[i] + " is NOT a palindrome.\n")
            
if __name__ == "__main__":
    main()