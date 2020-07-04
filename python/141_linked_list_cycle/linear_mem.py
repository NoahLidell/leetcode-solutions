# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        seen = set()
        if isinstance(head, type(None)):
                return False
        while True:
            if isinstance(head.next, type(None)):
                return False
            head_id = id(head)
            if head_id in seen:
                return True
            else:
                seen.add(head_id)
            head = head.next
