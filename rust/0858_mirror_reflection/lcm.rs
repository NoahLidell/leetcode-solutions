/*
858. Mirror Reflection
Medium

There is a special square room with mirrors on each of the four walls.  Except for the southwest corner, there are receptors on each of the remaining corners, numbered 0, 1, and 2.

The square room has walls of length p, and a laser ray from the southwest corner first meets the east wall at a distance q from the 0th receptor.

Return the number of the receptor that the ray meets first.  (It is guaranteed that the ray will meet a receptor eventually.)



Example 1:

Input: p = 2, q = 1
Output: 2
Explanation: The ray meets receptor 2 the first time it gets reflected back to the left wall.

Note:

    1 <= p <= 1000
    0 <= q <= p

*/
impl Solution {
    pub fn mirror_reflection(p: i32, q: i32) -> i32 {
        fn gcd(a: i32, b: i32) -> i32 {
            if a < b {
                let tmp = a;
                let a = b;
                let b = tmp;
            }
            if a % b == 0 {
                b
            } else {
                gcd(b, a % b)
            }
        }
        fn lcm(a: i32, b: i32) -> i32 {
            let p = a * b;
            p.abs() / gcd(a, b)
        }
        let mult = lcm(p, q);
        let v = mult / q;
        let h = mult / p;
        if v % 2 == 1 && h % 2 == 1 {
            1
        } else if h % 2 == 1 {
            2
        } else {
            0
        }
    }
}
