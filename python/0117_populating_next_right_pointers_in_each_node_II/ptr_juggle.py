"""
117. Populating Next Right Pointers in Each Node II
Medium

Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Follow up:

    You may only use constant extra space.
    Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.

 

Example 1:

Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

 

Constraints:

    The number of nodes in the given tree is less than 6000.
    -100 <= node.val <= 100

"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        head = root
        next_prev = None
        head2 = None
        while head:
            if not next_prev:
                if head.left:
                    next_prev = head.left
                    head2 = next_prev
                elif head.right:
                    next_prev = head.right
                    head2 = next_prev
                else:
                    head = head.next
            else:
                if head.left and head2 != head.right and head2 != head.left:
                    head2.next = head.left
                    head2 = head2.next
                elif head.right and head2 != head.right:
                    head2.next = head.right
                    head2 = head2.next
                else:
                    if head.next:
                        head = head.next
                    else:
                        head = next_prev
                        next_prev = None
        return root
