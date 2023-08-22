'''
Problem: Best Time to Buy and Sell Stock
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Language: Python
Written by: Anirudh Makhana
'''

##We need to make use of two pointers to solve this problem
##We will create a variable to store the minimum value and we will create a variable to store the maximum profit
##We will loop through the list and we will check if the current value is less than the minimum value
##If it is, we will update the minimum value
##Else, we will check if the difference between the current value and the minimum value is greater than the maximum profit
##If it is, we will update the maximum profit
##We will return the maximum profit

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        #Create a variable to store the minimum value:
        min_val = float('inf') ##You can also just use a really large number like 10**5
        
        #Create a variable to store the maximum profit:
        max_profit = 0
        #Loop through the list:
        for i, price in enumerate(prices):
            #Check if the current value is less than the minimum value:
            if price < min_val:
                #If it is, update the minimum value:
                min_val = price
            #Else, check if the difference between the current value and the minimum value is greater than the maximum profit:
            elif price - min_val > max_profit:
                #If it is, update the maximum profit:
                max_profit = price - min_val
        #Return the maximum profit:
        return max_profit
    
#Time Complexity: O(n)
#Space Complexity: O(1)

#Case 1:
#Input: prices = [7,1,5,3,6,4]
#Output: 5
print("Case 1:")
sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))
