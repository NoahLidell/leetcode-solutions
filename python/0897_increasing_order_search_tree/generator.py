"""
897. Increasing Order Search Tree
Easy

Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

 

Example 1:

Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

Example 2:

Input: root = [5,1,7]
Output: [1,null,5,null,7]

 

Constraints:

    The number of nodes in the given tree will be in the range [1, 100].
    0 <= Node.val <= 1000
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def traverse(node):
            if node.left:
                yield from traverse(node.left)
            yield node
            if node.right:
                yield  from traverse(node.right)
        res = head = None
        for n in traverse(root):
            if not head:
                res = n
                head = n
                head.left = None
            else:
                head.right = n
                head = head.right 
                head.left = None
        return res#         self.right = right
