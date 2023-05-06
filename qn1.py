"""
Author: Thomas 
Leetcode question 1: Two sum 

Time complexity: O(N)
Space complexity: O(N)

"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## dict to store index of int from num array 
        stored_num = {}
        
        ## Loop through array of int
        for i in range(len(nums)): 
            # Calculate the amount needed to achieve target 
            required_num = target - nums[i]
            # Check if required_num exist in stored_num array
            if required_num in stored_num: 
                # return index of current number and required_num 
                return [stored_num[required_num], i]
            # else return current number and index to stored_num dict 
            stored_num[nums[i]] = i

        # return empty list if no result 
        return []