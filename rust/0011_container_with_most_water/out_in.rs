use std::cmp::min;

impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {

        let mut left_idx = 0;
        let mut right_idx = height.len() - 1;
        let mut left = 0;
        let mut right = 0;
        let mut area = 0;
        loop {
            left = height[left_idx];
            right = height[right_idx];
            let width = right_idx - left_idx;
            let tmp = min(left, right) * width as i32;
            if tmp > area {
                area = tmp
            }
            if left >= right {
                right_idx -= 1;
            } else {
                left_idx += 1;
            }
            if left_idx >= right_idx {
                break
            }
        }
        area
    }
}
