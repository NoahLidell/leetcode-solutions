"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

Example 1:

Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:

Input: n = 1
Output: [[1]]

 

Constraints:

    1 <= n <= 20

"""
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        def next_dir():
            i = 0
            n = 4
            dirs = [(0,1), (1,0), (0,-1), (-1,0)]
            while True:
                yield dirs[i]
                i += 1
                i %= n
        direction = next_dir()
        matrix = [[0 for i in range(n)] for i in range(n)]
        pos = [0,-1]
        dy, dx = next(direction)
        for x in range(1,(n**2)+1):
            next_pos = [pos[0]+dy, pos[1]+dx]
            if (0 <= next_pos[0] < n) and (0 <= next_pos[1] < n) and matrix[next_pos[0]][next_pos[1]] == 0:
                pos = next_pos
                matrix[pos[0]][pos[1]] = x
            else:
                
                dy, dx = next(direction)
                pos = [pos[0]+dy, pos[1]+dx]
                matrix[pos[0]][pos[1]] = x
        return matrix
        
