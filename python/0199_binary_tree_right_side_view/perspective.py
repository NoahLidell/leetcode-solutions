"""
199. Binary Tree Right Side View
Medium

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        lvl = [root]
        nlvl = []
        right = []
        if not root: return []
        while lvl:
            node = lvl.pop(0)
            if node.left:
                nlvl.append(node.left)
            if node.right:
                nlvl.append(node.right)
            if not lvl:
                right.append(node.val)
                lvl = nlvl
                nlvl = []
        return right
