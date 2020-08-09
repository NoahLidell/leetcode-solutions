# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        from collections import deque
        q = deque()
        q.append((root.left, root.right))
        try:
            while (pair := q.popleft()):
                left, left_val = (pair[0], pair[0].val if pair[0] != None else None)
                rght, rght_val = (pair[1], pair[1].val if pair[1] != None else None)
                if left_val != rght_val:
                    return False
                if left and rght:
                    q.append((left.left, rght.right))
                    q.append((left.right, rght.left))
        except IndexError:
            pass
        return True
