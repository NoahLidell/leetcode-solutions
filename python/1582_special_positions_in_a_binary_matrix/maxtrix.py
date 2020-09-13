"""
511. Special Positions in a Binary Matrix
    Difficulty: Easy

Given a rows x cols matrix mat, where mat[i][j] is either 0 or 1, return the number of special positions in mat.

A position (i,j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

 

Example 1:

Input: mat = [[1,0,0],
              [0,0,1],
              [1,0,0]]
Output: 1
Explanation: (1,2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.

Example 2:

Input: mat = [[1,0,0],
              [0,1,0],
              [0,0,1]]
Output: 3
Explanation: (0,0), (1,1) and (2,2) are special positions. 

Example 3:

Input: mat = [[0,0,0,1],
              [1,0,0,0],
              [0,1,1,0],
              [0,0,0,0]]
Output: 2

Example 4:

Input: mat = [[0,0,0,0,0],
              [1,0,0,0,0],
              [0,1,0,0,0],
              [0,0,1,0,0],
              [0,0,0,1,1]]
Output: 3

 

Constraints:

    rows == mat.length
    cols == mat[i].length
    1 <= rows, cols <= 100
    mat[i][j] is 0 or 1.
"""


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        import numpy as np

        m = np.array(mat)
        soln = 0
        for i in range(len(m[0])):
            for j in range(len(m[:, 0])):
                if (
                    m[j][i] == 1
                    and len([n for n in m[:, i] if n == 1]) == 1
                    and len([n for n in m[j] if n == 1]) == 1
                ):
                    soln += 1
        return soln
