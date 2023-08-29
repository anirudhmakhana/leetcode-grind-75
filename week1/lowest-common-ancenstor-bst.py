'''
Problem: Lowest Common Ancestor of a Binary Search Tree
Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
Language: Python
Written by: Anirudh Makhana
'''

##Important NOTE
#For this problem, we need to make use of the property of a BST
#The property is that the left subtree of a node contains nodes with values less than the node's value
#The right subtree of a node contains nodes with values greater than the node's value
#The left and right subtree each must also be a BST
#We will create a function to perform dfs
#We will check if the node's value is greater than both the p and q values
#If it is, we will perform dfs on the left subtree
#Else, we will check if the node's value is less than both the p and q values
#If it is, we will perform dfs on the right subtree
#Else, we will return the node
#We will call the function on the root node

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ##Base condition:
        #Check if the node's value is greater than both the p and q values:
        if root.val > p.val and root.val > q.val:
            #If it is, perform dfs on the left subtree:
            return self.lowestCommonAncestor(root.left, p, q)
        #Else, check if the node's value is less than both the p and q values:
        elif root.val < p.val and root.val < q.val:
            #If it is, perform dfs on the right subtree:
            return self.lowestCommonAncestor(root.right, p, q)
        #Else, return the node:
        else:
            return root
        

# Case 1
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
sol = Solution()
nodes = [TreeNode(6), TreeNode(2), TreeNode(8), TreeNode(0), TreeNode(4), TreeNode(7), TreeNode(9), TreeNode(3), TreeNode(5)]
nodes[0].left = nodes[1]
nodes[0].right = nodes[2]
nodes[1].left = nodes[3]
nodes[1].right = nodes[4]
nodes[2].left = nodes[5]
nodes[2].right = nodes[6]
nodes[4].left = nodes[7]
nodes[4].right = nodes[8]
print(sol.lowestCommonAncestor(nodes[0], nodes[1], nodes[2]).val)
