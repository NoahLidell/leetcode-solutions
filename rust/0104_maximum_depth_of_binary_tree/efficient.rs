/*
104. Maximum Depth of Binary Tree
Easy

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.



Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:

Input: root = [1,null,2]
Output: 2

Example 3:

Input: root = []
Output: 0

Example 4:

Input: root = [0]
Output: 1



Constraints:

    The number of nodes in the tree is in the range [0, 104].
    -100 <= Node.val <= 100
*/
use std::cell::RefCell;
use std::cmp::max;
use std::rc::Rc;
impl Solution {
    pub fn max_depth(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn dfs(node: &Option<Rc<RefCell<TreeNode>>>, depth: i32, max_depth: &mut i32) {
            match node {
                Some(n) => {
                    let n = n.borrow();
                    *max_depth = max(*max_depth, depth);
                    dfs(&n.left, depth + 1, max_depth);
                    dfs(&n.right, depth + 1, max_depth);
                }
                None => {}
            }
        }
        let mut max_depth = 0;
        dfs(&root, 1, &mut max_depth);
        max_depth
    }
}
