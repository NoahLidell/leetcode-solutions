/*
289. Game of Life
Medium

According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

    Any live cell with fewer than two live neighbors dies as if caused by under-population.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by over-population.
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

 

Example 1:

Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

Example 2:

Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]

 

Constraints:

    m == board.length
    n == board[i].length
    1 <= m, n <= 25
    board[i][j] is 0 or 1.

 

Follow up:

    Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
    In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?

*/
impl Solution {
    pub fn game_of_life(board: &mut Vec<Vec<i32>>) {
        fn cell_gen(i: usize, j: usize, board: &mut Vec<Vec<i32>>) {
            let n = board.len() as i32;
            let m = board[0].len() as i32;
            let mut live_neighbors = 0;
            for di in -1..=1 {
                for dj in -1..=1 {
                    if !(di == 0 && dj == 0) {
                        let ii = i as i32 + di;
                        let jj = j as i32 + dj;
                        if ii >= 0 && jj >= 0 && ii < n && jj < m {
                            live_neighbors += board[ii as usize][jj as usize] % 2;
                        }   
                    }
                }
            }
            if board[i][j] == 1 {
                if live_neighbors < 2 || live_neighbors > 3 {
                    board[i][j] = 3; // was alive, dead next round
                }
            } else {
                if live_neighbors == 3 {
                    board[i][j] = 2; // was dead, alive next round
                }
            }
        }
        let n = board.len();
        let m = board[0].len();
        for i in 0..n {
            for j in 0..m {
                cell_gen(i,j, board);
            }
        }
        for i in 0..n {
            for j in 0..m {
                if board[i][j] > 1 {
                    board[i][j] = board[i][j] & 1 ^ 1;
                }
            }
        }
    }
}
