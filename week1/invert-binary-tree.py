'''
Problem: Invert Binary Tree
Link: https://leetcode.com/problems/invert-binary-tree/
Language: Python
Written by: Anirudh Makhana
'''

##We need to make use of recursion to solve this problem
##We will create a function to invert the binary tree
##We will check if the root is None
##If it is, we will return None
##Else, we will create a variable to store the left subtree
##We will create a variable to store the right subtree
##We will update the left subtree to the right subtree
##We will update the right subtree to the left subtree
##We will return the root

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        #Check if the root is None:
        if root is None:
            #If it is, return None:
            return None
        #Assign the left subtree to the right subtree and the right subtree to the left subtree:
        root.left, root.right = root.right, root.left
        #Invert the left subtree and the right subtree:
        self.invertTree(root.left)
        self.invertTree(root.right)
        #Return the root:
        return root
    
#Time Complexity: O(n)
#Space Complexity: O(n)

#Case 1:
#Input: root = [4,2,7,1,3,6,9]
#Output: [4,7,2,9,6,3,1]
print("Case 1:")
sol = Solution()
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)
print(sol.invertTree(root))
##Print out the nodes in the tree:
def print_tree(root):
    if root is None:
        return
    print(root.val)
    print_tree(root.left)
    print_tree(root.right)
print_tree(root)



