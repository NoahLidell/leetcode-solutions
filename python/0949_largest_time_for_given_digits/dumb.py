"""
949. Largest Time for Given Digits
Easy

Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

 

Example 1:

Input: [1,2,3,4]
Output: "23:41"

Example 2:

Input: [5,5,5,5]
Output: ""

 

Note:

    A.length == 4
    0 <= A[i] <= 9

"""
import copy
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        if min(A) > 2:
            return ''
        if 2 in A:
            chk2 = copy.deepcopy(A)
            chk2.remove(2)
            chkm = copy.deepcopy(chk2)
            if set([1,0,2,3]).intersection(set(chk2)):
                chkm.remove(max(set([1,0,2,3]).intersection(set(chk2))))
            chkm = [m for m in chkm if m<6]
        if 2 in A and set([1,0,2,3]).intersection(set(chk2)) and chkm != []:
            h1 = 2
            A.remove(2)
            h0 = max(set([1,0,2,3]).intersection(set(chk2)))
            A.remove(h0)
        else:
            try:
                h1 = max(set(A).intersection(set([0,1])))
            except ValueError:
                return ''
            A.remove(h1)
            h0 = max(set(A).intersection(set(range(10))))
            A.remove(h0)
        chkm = copy.deepcopy(A)
        chkm = [d for d in chkm if d <6]
        if chkm == []:
            return ''
        m1 = max(chkm)
        A.remove(m1)
        m0 = max(A)
        return f"{h1}{h0}:{m1}{m0}"
        
