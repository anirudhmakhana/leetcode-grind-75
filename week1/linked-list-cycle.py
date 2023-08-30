'''
Problem: Linked List Cycle
Link: https://leetcode.com/problems/linked-list-cycle/
Language: Python
Written by: Anirudh Makhana
'''

##We will create a function to check if a linked list has a cycle
#We can make use of Floyd's Tortoise and Hare Algorithm to solve this problem
#We will create two pointers, a slow pointer and a fast pointer
#The slow pointer will move one node at a time and the fast pointer will move two nodes at a time
#If the fast pointer reaches the end of the list, we will return False
#If the fast pointer and the slow pointer are equal, we will return True
#Else, we will return False
#Read more about the algorithm and illustration here: https://dev.to/alisabaj/floyd-s-tortoise-and-hare-algorithm-finding-a-cycle-in-a-linked-list-39af

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

##Function to check if a linked list has a cycle
class Solution(object):
    def hasCycle(self, head):
        #Create a slow pointer and a fast pointer:
        slow = head
        fast = head
        #Loop while the fast pointer is not None:
        while fast and fast.next:
            #Move the slow pointer one node at a time:
            slow = slow.next
            #Move the fast pointer two nodes at a time:
            fast = fast.next.next
            #Check if the fast pointer and the slow pointer are equal:
            if fast == slow:
                #If they are, return True
                return True
        #Return False
        return False
    
#Time Complexity: O(n)
#Space Complexity: O(1)

#Case 1:
#Input: head = [3,2,0,-4], pos = 1
#Output: true
print("Case 1:")
sol = Solution()
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next
print(sol.hasCycle(head))
