/*
593. Valid Square
Medium

Given the coordinates of four points in 2D space, return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True

 

Note:

    All the input integers are in the range [-10000, 10000].
    A valid square has four equal sides with positive length and four equal angles (90-degree angles).
    Input points have no order.
*/


use std::collections::HashSet;

impl Solution {
    pub fn valid_square(p1: Vec<i32>, p2: Vec<i32>, p3: Vec<i32>, p4: Vec<i32>) -> bool {
        fn dist(a: &Vec<i32>, b: &Vec<i32>) -> i32 {
            (a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1])
        }
        fn is_same(a: &Vec<i32>, b: &Vec<i32>) -> bool {
            a[0] == b[0] && a[1] == b[1]
        }
        let mut d = HashSet::new();
        if is_same(&p1,&p2) ||
           is_same(&p1,&p3) ||
           is_same(&p1,&p4) ||
           is_same(&p2,&p3) ||
           is_same(&p2,&p4) ||
           is_same(&p3,&p4) {
               return false
        }
        d.insert(dist(&p1,&p2));
        d.insert(dist(&p1,&p3));
        d.insert(dist(&p1,&p4));
        d.insert(dist(&p2,&p3));
        d.insert(dist(&p2,&p4));
        d.insert(dist(&p3,&p4));
        
        d.len() == 2
    }
}
