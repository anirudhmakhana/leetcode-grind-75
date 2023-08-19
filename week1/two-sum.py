'''
Leetcode Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/
Language: Python
Written by: Anirudh Makhana
'''

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Create a dictionary to store the values
        dict = {}
        # Loop through the list
        for i, num in enumerate(nums):
            # Check if the difference is in the dictionary
            if target - num in dict:
                # Return the index of the difference and the current index
                return [dict[target - num], i]
            # If the difference is not in the dictionary, add the current value to the dictionary
            dict[num] = i

# Time Complexity: O(n)
# Space Complexity: O(n)

sol = Solution()
print(sol.twoSum([2,7,11,15], 18))