# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        nodes = [[root]]
        try:
            values = [[root.val]]
        except AttributeError:
            return []
        symmetric = True
        #print(root)
        for row in nodes:
            next_row = []
            next_values = []
            #print(values)
            for n in row:
                if n.left:
                    next_row.append(n.left)
                    next_values.append(n.left.val)
                #else: 
                    #next_values.append(None)
                if n.right:
                    next_row.append(n.right)
                    next_values.append(n.right.val)
                #else:
                    #next_values.append(None)
            if next_row != []:
                nodes.append(next_row)
                values.append(next_values)
        return values
