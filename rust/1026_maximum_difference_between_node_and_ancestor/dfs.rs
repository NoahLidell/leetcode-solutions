/*
* Given the `root` of a binary tree, find the maximum value `V` for which there
* exist different nodes `A` and `B` where `V = |A.val - B.val|` and `A` is an
* ancestor of `B`.
*
* A node `A` is an ancestor of `B` if either: any child of `A` is equal to `B`, or
* any child of `A` is an ancestor of `B`.
*
*
* Example 1:
*
* []
* Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
* Output: 7
* Explanation: We have various ancestor-node differences, some of which are gi
* ven below :
* |8 - 3| = 5
* |3 - 7| = 4
* |8 - 1| = 7
* |10 - 13| = 3
* Among all possible differences, the maximum value of 7 is obtained by |8 - 1| =
* 7.
*
* Example 2:
*
* []
* Input: root = [1,null,2,null,0,3]
* Output: 3
*
*
* Constraints:
*
* * The number of nodes in the tree is in the range `[2, 5000]`.
* * `0 <= Node.val <= 105`
*
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
use std::cmp;
use std::rc::Rc;
impl Solution {
    pub fn max_ancestor_diff(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn chk(node: &Option<Rc<RefCell<TreeNode>>>, max: &mut i32, lower: i32, upper: i32) {
            let n = match node {
                Some(node) => node.borrow(),
                None => return,
            };
            let diff = cmp::max(n.val - lower, upper - n.val);
            if &diff > max {
                *max = diff
            }
            let lower = cmp::min(lower, n.val);
            let upper = cmp::max(upper, n.val);
            chk(&n.left, max, lower, upper);
            chk(&n.right, max, lower, upper);
        }
        let mut max = 0;
        let n = match &root {
            Some(root) => root.borrow(),
            None => return 0,
        };
        let base = &n.val;

        chk(&n.left, &mut max, *base, *base);
        chk(&n.right, &mut max, *base, *base);
        max
    }
}
