"""
Author: Thomas 
Leetcode question 9: Palindrome Number

Time complexity: O(N)
Space complexity: O(N)

"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Convert input to x 
        str_input = str(x) 

        # Check if str matches reverse str 
        if str_input == str_input[::-1]: 
            return True
        else: 
            return False