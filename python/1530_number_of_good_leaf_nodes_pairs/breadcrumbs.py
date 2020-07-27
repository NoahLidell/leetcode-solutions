# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from itertools import combinations
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        leaves = 0
        pairs = 0
        paths = []
        def recurse_to_leaf(node, path):
            nonlocal leaves
            nonlocal paths
            if left := node.left:
                if path:
                    next_path = [*path, "l"]
                else:
                    next_path = ["l"]
                recurse_to_leaf(left, next_path)
            if right := node.right:
                if path:
                    next_path = [*path, "r"]
                else:
                    next_path = ["r"]
                recurse_to_leaf(right, next_path)
            if not node.right and not node.left:
                leaves += 1
                paths.append(path)
        recurse_to_leaf(root, None)
        for a, b in combinations(paths, 2):
            for idx in range(0, max(len(a), len(b))):
                if a[idx] != b[idx]:
                    if len(a[idx:]) + len(b[idx:]) <= distance:
                        pairs += 1
                    break
        return pairs
        
