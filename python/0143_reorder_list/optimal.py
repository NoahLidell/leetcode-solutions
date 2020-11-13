"""
143. Reorder List
Medium

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.

Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return

        # find middle
        fast = head
        slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        rev = slow.next
        prev = None
        while rev:
            rev2 = rev.next
            rev.next = prev
            prev = rev
            rev = rev2
        slow.next = None

        # merge two halves
        head1 = head
        head2 = prev
        while head1 and head2:
            hn1 = head1.next
            hn2 = head2.next
            head1.next = head2
            head2.next = hn1
            head1 = hn1
            head2 = hn2
