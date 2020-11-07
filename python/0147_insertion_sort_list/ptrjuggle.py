"""
147. Insertion Sort List
Medium

Sort a linked list using insertion sort.


A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
 

Algorithm of Insertion Sort:

    Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
    At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
    It repeats until no input elements remain.


Example 1:

Input: 4->2->1->3
Output: 1->2->3->4

Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5

https://leetcode.com/problems/insertion-sort-list/
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        llist = ListNode()
        
        def insert(node):
            nonlocal llist
            p1 = llist.next
            p0 = llist
            while p1:
                if p1.val >= node.val:
                    p0.next = node
                    node.next = p1
                    return
                p1 = p1.next
                p0 = p0.next
            p0.next = node
            node.next = None
            
        while head:
            next_head = head.next
            insert(head)
            head = next_head
        
        return llist.next
