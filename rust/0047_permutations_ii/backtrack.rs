"""
47. Permutations II
Medium

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

 

Constraints:

    1 <= nums.length <= 8
    -10 <= nums[i] <= 10

"""
use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn permute_unique(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut counter: HashMap<i32, i32> = HashMap::new();
        let mut numbs: HashSet<i32> = HashSet::new();
        let size = nums.len();
        for n in nums {
            numbs.insert(n);
            let e = counter.entry(n).or_insert(0);
            *e += 1;
        }
        let mut permutes = vec![];
        fn btrack(arr: &mut Vec<i32>, counter: &mut HashMap<i32, i32>, soln: &mut Vec<Vec<i32>>, options: &HashSet<i32>, size: usize) {
            if arr.len() == size {
                soln.push(arr.clone());
            } else {
                for n in options {
                    let count = counter.entry(*n).or_insert(0);
                    if count > &mut 0 {
                        arr.push(*n);
                        *count -= 1;
                        btrack(arr, counter, soln, options, size);
                        let count = counter.entry(*n).or_insert(0);
                        *count += 1;
                        arr.pop();
                    }
                }
            }
        }
        let mut arr = vec![];
        btrack(&mut arr, &mut counter, &mut permutes, &numbs, size);
        permutes
    }
}
