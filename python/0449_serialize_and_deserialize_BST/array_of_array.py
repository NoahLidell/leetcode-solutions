"""
449. Serialize and Deserialize BST
Medium

Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

 

Example 1:

Input: root = [2,1,3]
Output: [2,1,3]

Example 2:

Input: root = []
Output: []

 

Constraints:

    The number of nodes in the tree is in the range [0, 104].
    0 <= Node.val <= 104
    The input tree is guaranteed to be a binary search tree.


https://leetcode.com/problems/serialize-and-deserialize-bst/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        s = ""
        nodes = deque([(0, "r", 0, root)])
        prev = -1
        while nodes:
            (level, side, parent, node) = nodes.popleft()
            if prev != level:
                c = 0
                prev = level
            if node:
                data = str(node.val)
                nodes.append((level + 1, "l", c, node.left))
                nodes.append((level + 1, "r", c, node.right))
            else:
                data = str(None)
            s += f"{level},{side},{parent},{data}|"
            c += 1
        return s[:-1]

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        tree = []
        lvl = -1
        print(data)
        s = data.split("|")
        for nodedata in s:
            level, side, pidx, nval = nodedata.split(",")
            level = int(level)
            pidx = int(pidx)
            if lvl != level:
                lvl = level
                tree.append([])
            if nval == "None":
                n = None
            else:
                n = TreeNode(int(nval))
            tree[lvl].append(n)
            if lvl == 0:
                continue
            if side == "l":
                tree[lvl - 1][pidx].left = tree[lvl][-1]
            else:
                tree[lvl - 1][pidx].right = tree[lvl][-1]
        return tree[0][0]
