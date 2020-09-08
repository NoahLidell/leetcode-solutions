/*1022. Sum of Root To Leaf Binary Numbers
Easy

Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

Return the sum of these numbers.



Example 1:

Input: [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22



Note:

    The number of nodes in the tree is between 1 and 1000.
    node.val is 0 or 1.
    The answer will not exceed 2^31 - 1.
*/
// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
//
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::cell::RefCell;
use std::rc::Rc;
impl Solution {
    pub fn sum_root_to_leaf(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let int = 0;
        let mut sum = 0;
        if let Some(n) = root {
            Self::dfs(n, int, &mut sum);
        }
        sum
    }
    fn dfs(n: Rc<RefCell<TreeNode>>, int: i32, sum: &mut i32) {
        let next_int = (int << 1) | n.borrow().val;
        if n.borrow().left.is_none() && n.borrow().right.is_none() {
            *sum += next_int;
        } else {
            if let Some(l) = n.borrow().left.clone() {
                Self::dfs(l, next_int, sum);
            }
            if let Some(r) = n.borrow().right.clone() {
                Self::dfs(r, next_int, sum);
            }
        }
    }
}
