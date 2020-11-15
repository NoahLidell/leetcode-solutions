"""
938. Range Sum of BST
Easy

Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].

 

Example 1:

Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32

Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23

 

Constraints:

    The number of nodes in the tree is in the range [1, 2 * 104].
    1 <= Node.val <= 105
    1 <= low <= high <= 105
    All Node.val are unique.
"""

use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn range_sum_bst(root: Option<Rc<RefCell<TreeNode>>>, low: i32, high: i32) -> i32 {
        let mut sum = 0;
        fn dfsum(node: &Option<Rc<RefCell<TreeNode>>>, low: i32, high: i32, sum: &mut i32) {
            if let Some(n) = node {
                let n = n.borrow();
                if n.val >= low && n.val <= high {
                    *sum += n.val;
                }
                dfsum(&n.left, low, high, sum);
                dfsum(&n.right, low, high, sum);
            }
        }
        dfsum(&root, low, high, &mut sum);
        sum
    }
}
