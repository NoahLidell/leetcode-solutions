"""
445. Add Two Numbers II
Medium

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = n2 = 0
        while l1:
            n1 *= 10
            n1 += l1.val
            l1 = l1.next
        while l2:
            n2 *= 10
            n2 += l2.val
            l2 = l2.next
        if not (n1 or n2):
            return ListNode(0)
        carry = 0
        out = None
        while n1 or n2 or carry:
            d1 = n1 % 10
            n1 //= 10
            d2 = n2 % 10
            n2 //= 10
            carry, d = divmod(d1 + d2 + carry, 10)
            node = ListNode(d, out)
            out = node
        return out
