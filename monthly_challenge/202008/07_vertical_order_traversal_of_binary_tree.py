"""
Given a binary tree, return the vertical order traversal of its nodes values.

For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).

Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, we report the values of the nodes in order from top to bottom (decreasing Y coordinates).

If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.

Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        nodes = {}
        def dfs(node, x, y):
            nonlocal nodes
            nodes.setdefault(x, []).append((node.val, y))
            if node.left:
                dfs(node.left, x-1, y-1)
            if node.right:
                dfs(node.right, x+1, y-1)
        dfs(root, 0, 0)
        lis = [(i, v) for i,v in nodes.items()]
        lis.sort(key=lambda x: x[0])
        lis = [v[1] for v in lis]
        output = []
        for l in lis:
            #l.sort(key=lambda x: (abs(x[1])+x[0]))
            ytrack = {}
            for v in l:
                ytrack.setdefault(abs(v[1]), []).append(v[0])
            yout = []
            for idx in range(min(ytrack.keys()), max(ytrack.keys())+1):
                if ylis := ytrack.get(idx):
                    ylis.sort()
                    yout = yout + ylis
            output.append(yout)
        return output
        
