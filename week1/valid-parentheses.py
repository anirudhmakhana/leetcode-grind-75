'''
Leetcode: Valid Parentheses
Link: https://leetcode.com/problems/valid-parentheses/
Language: Python
Written by: Anirudh Makhana
'''

##We need to make use of stacks to solve this problem
##We will use a stack to store the values and we will pop the values from the stack if the closing bracket is found

class Solution:
    def isValid(self, s):
        #Create a stack to store the values:
        stack = []
        #Create a dictonary for the pairs:
        mappings = {'(':')', '{':'}','[':']'}
        #Loop through the string:
        for i, char in enumerate(s):
            #Check if the character is in the mappings:
            if char in mappings:
                #If it is, append it to the stack:
                stack.append(char)
            #Else, check if the stack is empty or if the character is not equal to the last element in the stack:
            else:
                if not stack or mappings[stack.pop()] != char:
                    return False
        return not stack
    
#Time Complexity: O(n)
#Space Complexity: O(n)

sol = Solution()
print(sol.isValid("()[]{}"))
print(sol.isValid("([)]"))