"""
1329. Sort the Matrix Diagonally
Medium

A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.

 

Example 1:

Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]

 

Constraints:

    m == mat.length
    n == mat[i].length
    1 <= m, n <= 100
    1 <= mat[i][j] <= 100

"""


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        mi = m
        ni = 0

        while mi >= 0 and ni < n:
            i = mi
            j = ni
            diag = []
            while i < m and j < n:
                diag.append(mat[i][j])
                i += 1
                j += 1
            diag.sort()
            i = mi
            j = ni
            while diag:
                mat[i][j] = diag.pop(0)
                i += 1
                j += 1
            if mi == 0:
                ni += 1
            else:
                mi -= 1

        return mat
