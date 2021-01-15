"""
82. Remove Duplicates from Sorted List II
Medium

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

 

Example 1:

Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:

Input: head = [1,1,1,2,3]
Output: [2,3]

 

Constraints:

    The number of nodes in the list is in the range [0, 300].
    -100 <= Node.val <= 100
    The list is guaranteed to be sorted in ascending order.

"""


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        root = ListNode()
        root.next = head
        back = root
        while head and head.next:
            h = head.next
            prev = None
            while h and head.val == h.val:
                prev = h
                h = h.next
            if prev != None:  # then there are dupes
                back.next = h
                head = h
            else:
                back = head
                head = head.next
        return root.next
