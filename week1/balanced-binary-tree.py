'''
Problem: Balanced Binary Tree
Link: https://leetcode.com/problems/balanced-binary-tree/
Language: Python
Written by: Anirudh Makhana
'''

##We will create a function to check if a tree is balanced
##We will create a function to get the height of a tree
##A height balanced tree is a tree in which the left and right subtrees of every node differ in height by no more than 1

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    ##Function to get the height of a tree
    def get_depth(self, node):
        #Check if the node is None:
        if node is None:
            #If it is, return 0
            return 0
        #Else, return 1 + the maximum of the height of the left subtree and the height of the right subtree
        return 1 + max(self.get_depth(node.left), self.get_depth(node.right))
    def isBalanced(self, root):
        #Check if the root is None:
        if root is None:
            #If it is, return True
            return True
        #Else, check if the absolute difference between the height of the left subtree and the height of the right subtree is less than or equal to 1
        if abs(self.get_depth(root.left) - self.get_depth(root.right)) <= 1:
            #If it is, return True
            return True
        #Else, return False
        return False
    
#Time Complexity: O(n^2)
#Space Complexity: O(n)

#Case 1:
#Input: root = [3,9,20,null,null,15,7]
#Output: true
print("Case 1:")
sol = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right= TreeNode(7)
print(sol.isBalanced(root))
