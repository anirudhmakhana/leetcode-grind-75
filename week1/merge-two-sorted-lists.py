'''
Leetcode: Merge Two Sorted Lists
Link: https://leetcode.com/problems/merge-two-sorted-lists/
Language: Python
Written by: Anirudh Makhana
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

##We need to make use of two pointers to solve this problem
##We will create a dummy node and we will compare the values of the two lists and append the smaller value to the dummy node
##We will then move the pointer of the list with the smaller value to the next node and we will repeat the process until we reach the end of one of the lists
##We will then append the remaining nodes of the other list to the dummy node

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #Create a dummy node:
        dummy = ListNode()
        #Create a pointer to the dummy node:
        curr = dummy
        #Loop through the two lists:
        while l1 and l2:
            #Check which value is smaller:
            if l1.val < l2.val:
                #Append the smaller value to the dummy node:
                curr.next = l1
                #Move the pointer of the list with the smaller value to the next node:
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            #Move the pointer of the dummy node to the next node:
            curr = curr.next
        #Append the remaining nodes of the other list to the dummy node:
        curr.next = l1 or l2
        #Return the next node of the dummy node:
        return dummy.next

#Complexity Analysis:
'''
 n = no of nodes in list1
 m = no of nodes in list2
'''
#Time Complexity: O(n + m)
#Space Complexity: O(1)

#Case 1:
#Input: l1 = [1,2,4], l2 = [1,3,4]
#Output: [1,1,2,3,4,4]
print("Case 1:")
l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
sol = Solution()
result = sol.mergeTwoLists(l1, l2)
while result:
    print(result.val)
    result = result.next