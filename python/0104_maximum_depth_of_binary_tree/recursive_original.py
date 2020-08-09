# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def depth(n: TreeNode, depth_count: int) -> int:
            if (not n.left) and (not n.right):
                return depth_count
            elif n.left and n.right:
                left = depth(n.left, depth_count+1)
                right = depth(n.right, depth_count+1)
                return max(left, right)
            elif n.left: 
                return depth(n.left, depth_count+1)
            else:
                return depth(n.right, depth_count+1)
        if not root:
            return 0
        return depth(root, 1)
