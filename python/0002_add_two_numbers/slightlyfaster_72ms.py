# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        nodes = ListNode(0)
        end = nodes
        while l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            carry, digit = divmod(carry, 10)
            end.val = digit
            #print((l1.next if l1 else None), (l2.next if l2 else None))
            if carry or l1 or l2:
               
                end.next = ListNode(carry)
                end = end.next
            else: break
        return nodes
            
