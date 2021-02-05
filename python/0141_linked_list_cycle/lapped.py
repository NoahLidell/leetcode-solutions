# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
		slow = head
        if head:
            fast = head.next
        else:
            fast = None
        while fast and slow:
            if fast == slow:
                return True
            else:
                if fast.next:
                    fast = fast.next.next
                else:
                    fast = fast.next
                slow = slow.next
        return False
