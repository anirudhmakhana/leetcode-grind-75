'''
Problem: Valid Anagram
Link: https://leetcode.com/problems/valid-anagram/
Language: Python
Written by: Anirudh Makhana
'''

##We need to make use of a dictionary to solve this problem
##We will create a dictionary to store the characters in the string and their frequencies
##We will loop through the characters in the string
##We will check if the character is in the dictionary
##If it is, we will increment the frequency
##Else, we will set the frequency to 1
##We will loop through the characters in the string
##We will check if the character is in the dictionary
##If it is, we will decrement the frequency
##Else, we will return False
##We will loop through the keys in the dictionary
##We will check if the frequency is not 0
##If it is not, we will return False
##Else, we will return True


class Solution():
    def isAnagram(self, s: str, t: str) -> bool:
        #Check if the length of the strings are equal:
        if len(s) != len(t):
            #If they are not, return False:
            return False
        #Create a dictionary to store the characters in the string and their frequencies:
        s_dict = {}
        #Loop through the characters in the string:
        for char in s:
            #Check if the character is in the dictionary:
            if char in s_dict:
                #If it is, increment the frequency:
                s_dict[char] += 1
            else:
                #Else, set the frequency to 1:
                s_dict[char] = 1
        #Loop through the characters in the string:
        for char in t:
            #Check if the character is in the dictionary:
            if char in s_dict:
                #If it is, decrement the frequency:
                s_dict[char] -= 1
            else:
                #Else, return False:
                return False
        #Loop through the keys in the dictionary:
        for key in s_dict:
            #Check if the frequency is not 0:
            if s_dict[key] != 0:
                #If it is not, return False:
                return False
        #Return True:
        return True
    
#Time Complexity: O(n)
#Space Complexity: O(n)

#Case 1:
#Input: s = "anagram", t = "nagaram"
#Output: true
print("Case 1:")
sol = Solution()
s = "anagram"
t = "nagaram"
print(sol.isAnagram(s, t))
