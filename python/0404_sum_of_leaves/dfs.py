"""
Sum of Left Leaves

Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        left_sum = 0
        def dfs(node, side):
            nonlocal left_sum
            if node.left == None and node.right == None and side == 1:
                left_sum += node.val
            if node.left:
                dfs(node.left, 1)
            if node.right:
                dfs(node.right, 2)
        if root:
            dfs(root, 3)
        return left_sum

