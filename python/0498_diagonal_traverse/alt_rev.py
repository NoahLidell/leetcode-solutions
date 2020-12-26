"""
498. Diagonal Traverse
Medium

Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

 

Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Explanation:

 

Note:

The total number of elements of the given matrix will not exceed 10,000.
"""


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        diag = []
        m = len(matrix)
        n = len(matrix[0])
        x = y = 0
        while (x, y) != (n - 1, m - 1):
            diag.append((y, x))
            if x != n - 1:
                x += 1
            else:
                y += 1
        else:
            diag.append((y, x))

        nums = []
        c = 0
        for y, x in diag:
            dnums = []
            while (0 <= x < n) and (0 <= y < m):
                dnums.append(matrix[y][x])
                x -= 1
                y += 1
            if c % 2 == 0:
                nums.extend(dnums[::-1])
            else:
                nums.extend(dnums)
            c += 1

        return nums
