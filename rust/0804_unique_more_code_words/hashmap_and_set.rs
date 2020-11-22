/*
804. Unique Morse Code Words
Easy

International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cab" can be written as "-.-..--...", (which is the concatenation "-.-." + ".-" + "-..."). We'll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.

Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation:
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".

Note:

    The length of words will be at most 100.
    Each words[i] will have length in range [1, 12].
    words[i] will only consist of lowercase letters.
*/
use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn unique_morse_representations(words: Vec<String>) -> i32 {
        let morse = vec![
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..",
            "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-",
            "-.--", "--..",
        ]
        .into_iter()
        .map(|x| String::from(x))
        .collect::<Vec<String>>();
        let alpha = String::from("abcdefghijklmnopqrstuvwxyz");
        let lookup: HashMap<char, String> = alpha.chars().zip(morse.into_iter()).collect();
        let mut strings: HashSet<String> = HashSet::new();
        words.into_iter().for_each(|w| {
            let mut morse_word = String::new();
            for c in w.chars() {
                morse_word.push_str(lookup.get(&c).unwrap());
            }
            strings.insert(morse_word);
        });
        strings.len() as i32
    }
}
