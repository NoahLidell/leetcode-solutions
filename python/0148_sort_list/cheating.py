"""
148. Sort List
Medium

Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

 

 Example 1:

 Input: head = [4,2,1,3]
 Output: [1,2,3,4]

 Example 2:

 Input: head = [-1,5,3,4,0]
 Output: [-1,0,3,4,5]

 Example 3:

 Input: head = []
 Output: []

  

  Constraints:

      The number of nodes in the list is in the range [0, 5 * 104].
      -105 <= Node.val <= 105

https://leetcode.com/problems/sort-list/
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        scratch = []
        if not head:
            return None
        while head:
            scratch.append((head, head.val))
            head = head.next
        scratch.sort(key=lambda x: x[1])
        for i in range(len(scratch)):
            if i != 0:
                scratch[i-1][0].next = scratch[i][0]
                
        scratch[-1][0].next = None
        return scratch[0][0]
