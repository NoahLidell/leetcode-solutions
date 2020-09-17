"""
1041. Robot Bounded In Circle
Medium

On an infinite plane, a robot initially stands at (0, 0) and faces north.  The robot can receive one of three instructions:

    "G": go straight 1 unit;
    "L": turn 90 degrees to the left;
    "R": turn 90 degress to the right.

The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

 

Example 1:

Input: "GGLLGG"
Output: true
Explanation: 
The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.

Example 2:

Input: "GG"
Output: false
Explanation: 
The robot moves north indefinitely.

Example 3:

Input: "GL"
Output: true
Explanation: 
The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...
"""
from collections import deque


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = deque(["E", "S", "W", "N"])

        def rotate(d):
            if d == "R":
                tmp = directions.pop()
                directions.appendleft(tmp)
            else:
                tmp = directions.popleft()
                directions.append(tmp)

        loc = [0, 0]
        for d in list(instructions):
            if d != "G":
                rotate(d)
            else:
                if directions[0] == "E":
                    loc[1] += 1
                elif directions[0] == "S":
                    loc[0] -= 1
                elif directions[0] == "W":
                    loc[1] -= 1
                else:
                    loc[0] += 1
        if loc == [0, 0]:
            return True
        elif directions[0] == "E":
            return False
        else:
            return True
