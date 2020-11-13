"""
Reorder List

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
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return None
        idx_map = {}
        idx = 0
        pointer = head
        while 1:
            idx_map[idx] = pointer
            idx += 1
            pointer = pointer.next
            if pointer == None:
                break
        low_idx = 0
        high_idx = idx - 1
        while 1:
            low =  idx_map[low_idx]
            high = idx_map[high_idx]
            low.next = high
            low_idx += 1
            if low_idx == high_idx:
                high.next = None
                break
            low =  idx_map[low_idx]
            high.next = low
            high_idx -= 1
            if low_idx == high_idx:
                low.next = None
                break
            
