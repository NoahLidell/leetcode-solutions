"""
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        found = 0
        def dfs(node, path_sums=[]):
            nonlocal found
            nonlocal sum
            n = node.val
            if n == sum:
                found += 1
            next_path_sums = [n]
            for path_sum in path_sums:
                new_sum = n + path_sum
                if new_sum == sum:
                    found += 1
                next_path_sums.append(new_sum)
            if left := node.left:
                dfs(left, next_path_sums)
            if right := node.right:
                dfs(right, next_path_sums)
        if root:
            dfs(root)
        return found
 
