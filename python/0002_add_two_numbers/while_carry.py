# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        root = ListNode()
        head = root
        while l1 or l2:
            if l1:
                n1 = l1.val
                l1 = l1.next
            else:
                n1 = 0
            if l2:
                n2 = l2.val
                l2 = l2.next
            else:
                n2 = 0
            s = n2 + n1 + carry
            head.next = ListNode(s % 10)
            head = head.next
            carry = s // 10
        if carry:
            head.next = ListNode(carry)
        return root.next
