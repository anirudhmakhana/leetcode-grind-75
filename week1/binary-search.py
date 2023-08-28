'''
Problem: Binary Search
Link: https://leetcode.com/problems/binary-search/
Language: Python
Written by: Anirudh Makhana
'''

##We need to make use of binary search to solve this problem
##We will create a function to perform binary search
##We will create a variable to store the left pointer
##We will create a variable to store the right pointer
##We will loop while the left pointer is less than or equal to the right pointer
##We will create a variable to store the middle pointer
##We will check if the value at the middle pointer is equal to the target
##If it is, we will return the middle pointer
##Else, we will check if the value at the middle pointer is less than the target
##If it is, we will update the left pointer to the middle pointer + 1
##Else, we will update the right pointer to the middle pointer - 1
##We will return -1

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        #Create a variable to store the left pointer:
        left = 0
        #Create a variable to store the right pointer:
        right = len(nums) - 1
        #Loop while the left pointer is less than or equal to the right pointer:
        while left <= right:
            #Create a variable to store the middle pointer:
            mid = (left + right) // 2
            #Check if the value at the middle pointer is equal to the target:
            if nums[mid] == target:
                #If it is, return the middle pointer:
                return mid
            #Else, check if the value at the middle pointer is less than the target:
            elif nums[mid] < target:
                #If it is, update the left pointer to the middle pointer + 1:
                left = mid + 1
            else:
                #Else, update the right pointer to the middle pointer - 1:
                right = mid - 1
        #Return -1:
        return -1
    
#Time Complexity: O(log n)
#Space Complexity: O(1)

#Case 1:
#Input: nums = [-1,0,3,5,9,12], target = 9
#Output: 4
print("Case 1:")
sol = Solution()
nums = [-1,0,3,5,9,12]
target = 9
print(sol.search(nums, target))
