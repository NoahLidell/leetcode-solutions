/*
556. Next Greater Element III
Medium

Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.

 

Example 1:

Input: n = 12
Output: 21

Example 2:

Input: n = 21
Output: -1

 

Constraints:

    1 <= n <= 231 - 1

*/
impl Solution {
    pub fn next_greater_element(n: i32) -> i32 {
        if n <= 10 {
            return -1
        }
        let mut n = n;
        // work in 64 bit int land to avoid overflow errors
        let mut digits: Vec<i64> = vec![];
        
        // put digits in a vec
        while n > 0 {
            digits.push((n % 10).into());
            n /= 10;
        }
        let mut big = -1;
        let mut big_idx = 0usize;
        let mut smol_idx = 0usize;
        
        // find the first instance of a smaller digit being 
        // at a higher decimal place than a larger digit
        // these are the "misplaced digits"
        for (idx, val) in digits.iter().enumerate() {
            if val >= &big {
                big = *val;
                big_idx = idx;
            } else if val < &big {
                smol_idx = idx;
                break;
            }
        }
        // edge case: return -1 if above condition doesn't exist
        if smol_idx == 0 {
            return -1
        }
        
        // sort the misplaced digits vec so larger 
        // digits occur at smaller decimal places
        let mut misplaced = digits[0..=smol_idx].to_owned();
        misplaced.sort_by(|a,b| b.cmp(a));
        
        // extract the digit directly greater than
        // the most significant digit in the original
        // slice of misplaced digits and place it 
        // in the original digits array
        for i in 0..=smol_idx {
            if misplaced[i] == digits[smol_idx] {
                digits[smol_idx] = misplaced.remove(i-1);
                break;
            }
        }
        
        // place the remaining digits, correctly placed
        // from high to low in the original digits vec
        digits[..smol_idx].swap_with_slice(&mut misplaced);
        
        // rebuild i32 from vec of digits
        let mut out = 0i64;
        let mut place = 1;
        for d in digits {
            out += d*place;
            place *= 10;
        }
        
        // edge case: handle i32 overflow
        if out > std::i32::MAX as i64 {
            -1
        } else {
            out as i32
        }
    }
}
