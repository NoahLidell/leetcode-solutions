"""
Random Point in Non-overlapping Rectangles

Given a list of non-overlapping axis-aligned rectangles rects, write a function pick which randomly and uniformily picks an integer point in the space covered by the rectangles.

Note:

    An integer point is a point that has integer coordinates. 
    A point on the perimeter of a rectangle is included in the space covered by the rectangles. 
    ith rectangle = rects[i] = [x1,y1,x2,y2], where [x1, y1] are the integer coordinates of the bottom-left corner, and [x2, y2] are the integer coordinates of the top-right corner.
    length and width of each rectangle does not exceed 2000.
    1 <= rects.length <= 100
    pick return a point as an array of integer coordinates [p_x, p_y]
    pick is called at most 10000 times.

Example 1:

Input: 
["Solution","pick","pick","pick"]
[[[[1,1,5,5]]],[],[],[]]
Output: 
[null,[4,1],[4,1],[3,3]]

Example 2:

Input: 
["Solution","pick","pick","pick","pick","pick"]
[[[[-2,-2,-1,-1],[1,0,3,0]]],[],[],[],[],[]]
Output: 
[null,[-1,-2],[2,0],[-2,-1],[3,0],[-2,-2]]

Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array of rectangles rects. pick has no arguments. Arguments are always wrapped with a list, even if there aren't any.
 
"""
class Solution:
    from random import choices, choice

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.dist = []
        for i, r in enumerate(rects):
            x_max, x_min = max(r[0], r[2]), min(r[0], r[2]) 
            y_max, y_min = max(r[1], r[3]), min(r[1], r[3])
            x_size = x_max - x_min + 1
            y_size = y_max - y_min + 1
            size = x_size * y_size
            self.dist.append(size)

        

    def pick(self) -> List[int]:
        r = choices(self.rects, weights=self.dist)
        r = r[0]
        x = choice(range(r[0], r[2]+1))
        y = choice(range(r[1], r[3]+1))
        return [x,y]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()

