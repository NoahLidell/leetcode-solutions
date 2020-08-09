# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        soln = ListNode(0)
        head = soln
        if not l1 and not l2:
            return None
        while l1 or l2:
            v1 = l1.val if l1 else None
            v2 = l2.val if l2 else None
            if (l1 != None) and (l2 != None):
                if v1 < v2:
                    head.val = v1
                    l1 = l1.next
                else:
                    head.val = v2
                    l2 = l2.next
            elif v1 != None:
                head.val = v1
                l1 = l1.next
            elif v2 != None:
                head.val = v2
                l2 = l2.next
            if l1 or l2:
                head.next = ListNode(0)
                head = head.next
        return soln
