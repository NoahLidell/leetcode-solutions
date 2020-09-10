/*
299. Bulls and Cows
Easy

You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. 

Please note that both secret number and friend's guess may contain duplicate digits.

Example 1:

Input: secret = "1807", guess = "7810"

Output: "1A3B"

Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.

Example 2:

Input: secret = "1123", guess = "0111"

Output: "1A1B"

Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.

Note: You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.
*/
use std::collections::HashSet;

impl Solution {
    pub fn get_hint(secret: String, guess: String) -> String {
        let idx_chars: HashSet<(usize, char)> = secret.chars().enumerate().collect();
        let mut secret: Vec<char> = secret.chars().collect();
        let mut bulls: Vec<char> = vec![];
        let mut cows: Vec<char> = vec![];
        let mut bull_idx: Vec<usize> = vec![];
        
        for c in guess.chars().enumerate() {
            if idx_chars.contains(&c) {
                bull_idx.push(c.0);
                bulls.push(c.1);
            }
        }
        let mut guess: Vec<char> = guess.chars().collect();
        bull_idx.sort_by(|a,b| b.cmp(a));
        for idx in bull_idx.into_iter() {
            secret.remove(idx);
            guess.remove(idx);
        }
        for c in guess.into_iter() {
            match secret.iter().position(|&x| x == c) {
                Some(idx) => {
                    secret.remove(idx);
                    cows.push(c);
                },
                None => (),
            }
        }
        format!("{}A{}B", bulls.len(), cows.len())
    }
}
