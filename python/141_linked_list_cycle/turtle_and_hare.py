# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        try:
            turtle = head
            hare = head.next
            while turtle != hare:
                turtle = turtle.next
                hare = hare.next.next
            return True
        except:
            return False
