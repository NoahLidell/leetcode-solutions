"""
21. Merge Two Sorted Lists
Easy

Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

 

Example 1:

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: l1 = [], l2 = []
Output: []

Example 3:

Input: l1 = [], l2 = [0]
Output: [0]

 

Constraints:

    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both l1 and l2 are sorted in non-decreasing order.

"""


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = ListNode()
        base = root
        while l1 or l2:
            if l2 and l1:
                if l2.val < l1.val:
                    root.next = l2
                    l2 = l2.next
                else:
                    root.next = l1
                    l1 = l1.next
                root = root.next
            else:
                if l1:
                    root.next = l1
                else:
                    root.next = l2
                break
        return base.next
