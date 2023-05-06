"""
Author: Thomas 
Leetcode question 13: Roman to Integer

Time complexity: O(N)
Space complexity: O(1)

"""
class Solution:
    def romanToInt(self, s: str) -> int:
        # Create a dict to store roman numerals
        r_list = {"I": 1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        result = 0 
        prev_val = 0

        # Loop through roman numeral string from right to left 
        for i in range(len(s) -1, -1, -1):
            # Check if current val is smaller than previous value; 
            if r_list[s[i]] < prev_val: 
                # Subtract from result 
                result -= r_list[s[i]]
            else: 
                # Add to result 
                result += r_list[s[i]]
            # Update the previous value to current val
            prev_val = r_list[s[i]]
        return result
