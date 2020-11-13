"""
46. Permutations
Medium

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

"""
impl Solution {
    pub fn permute(mut nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut permutes = vec![];
        let n = nums.len();
        fn permute(arr: &mut Vec<i32>, size: usize, soln: &mut Vec<Vec<i32>>) {
            if size == 0 {
                soln.push(arr.clone());
            } else {
                permute(arr, size-1, soln);
                /* if size is odd swap first and last element
                   if size is even swap the ith and last element */
                for i in 0..size-1 {
                    if (size & 1) != 0 {
                        arr.swap(0, size-1);
                    } else {
                        arr.swap(i, size-1);
                    }
                    permute(arr, size-1, soln);
                }
            }
        }
        permute(&mut nums, n, &mut permutes);
        permutes
    }
}
