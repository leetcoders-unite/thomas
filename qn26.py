"""
Author: Thomas 
Leetcode question 26: Remove Duplicates from Sorted Array

Time complexity: O(N)
Space complexity: O(1)

"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # initialize and store previous array element 
        unique_ctr = 0

        # Loop through nums array 
        for curr_val in range(1, len(nums)): 
            # Check current val and previous val 
            if nums[curr_val] != nums[unique_ctr]: 
                # If not the same, count + 1
                unique_ctr += 1
                # print(num_unique_elements)
                nums[unique_ctr] = nums[curr_val]

        return unique_ctr + 1