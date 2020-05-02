# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        nodes = None
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            carry, digit = int(carry/10), int(carry%10)
            if not nodes:
                nodes = ListNode(digit, next=None)
                end = nodes
            else:
                end.next = ListNode(digit, next=None)
                end = end.next
        return nodes
