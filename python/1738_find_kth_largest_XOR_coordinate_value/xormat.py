"""
1738. Find Kth Largest XOR Coordinate Value
Medium

You are given a 2D matrix of size m x n, consisting of non-negative integers. You are also given an integer k.

The value of coordinate (a, b) of the matrix is the XOR of all matrix[i][j] where 0 <= i <= a < m and 0 <= j <= b < n (0-indexed).

Find the kth largest value (1-indexed) of all the coordinates of matrix.

 

Example 1:

Input: matrix = [[5,2],[1,6]], k = 1
Output: 7
Explanation: The value of coordinate (0,1) is 5 XOR 2 = 7, which is the largest value.

Example 2:

Input: matrix = [[5,2],[1,6]], k = 2
Output: 5
Explanation: The value of coordinate (0,0) is 5 = 5, which is the 2nd largest value.

Example 3:

Input: matrix = [[5,2],[1,6]], k = 3
Output: 4
Explanation: The value of coordinate (1,0) is 5 XOR 1 = 4, which is the 3rd largest value.

Example 4:

Input: matrix = [[5,2],[1,6]], k = 4
Output: 0
Explanation: The value of coordinate (1,1) is 5 XOR 2 XOR 1 XOR 6 = 0, which is the 4th largest value.

 

Constraints:

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 1000
    0 <= matrix[i][j] <= 106
    1 <= k <= m * n

"""
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        vals = []
        xormat = []
        for row in matrix:
            xor = row.pop(0)
            if xormat:
                xorrow = [xor ^ xormat[-1][0]]
            else:
                xorrow = [xor]
            for i, n in enumerate(row):
                xor ^= n
                if xormat:
                     xorrow.append(xor ^ xormat[-1][i+1])
                else:
                    xorrow.append(xor)
            xormat.append(xorrow)
        
        m = len(matrix)
        n = len(xormat[0])
        """
        for i in range(m):
            for j in range(n):
                rows = [r[j] for r in xormat[:i+1]]
                xor = rows.pop(0)
                print(i,j,rows,xor)
                vals.append(xor)
                while rows:
                    xor ^= rows.pop(0)
                    vals.append(xor)"""
        """for i in range(m):
            rows = [ r for r in xormat[:i+1]]
            print(rows)
            r0 = rows.pop(0)
            for j in range(n):
                xor = r0[j]
                print(xor, i,j)
                vals.append(xor)
                for r in rows:
                    xor ^= r[j]
                    vals.append(xor)
            print(vals)"""
        for i in range(m):
            for j in range(n):
                vals.append(xormat[i][j])
        vals.sort(reverse=True)
        return vals[k-1]
