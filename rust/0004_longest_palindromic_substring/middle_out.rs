impl Solution {
    pub fn longest_palindrome(s: String) -> String {
        let slen = s.len();
        if slen <= 1 {
            return s
        }
        let mut max = 1;
        let mut pal = &s[0..1];
        if slen == 2 {
            if &s[0..1] == &s[1..2] {
                return s
            } else {
                return pal.to_string()
            }
        }
        for i in 1..slen {
            let mut plus = 1;
            let mut minus = 1;
            let c = &s[i..i+1];
            if max == 1 && i == 1 && c == &s[0..1] {
                max = 2;
                pal = &s[0..2]; 
            } 
            if i+2 <= slen {
                if c == &s[i+1..i+2] {
                    let mut tmp_plus = 2;
                    let mut tmp_minus = 1;
                    if max == 1 {
                        max = 2;
                        pal = &s[i..i+2]
                    }
                    while i-tmp_minus >= 0 && i+tmp_plus < slen {
                        let char0 = &s[i-tmp_minus..i-tmp_minus+1];
                        let char1 = &s[i+tmp_plus..i+tmp_plus+1];
                        if char0 == char1 && tmp_plus+1+tmp_minus > max {
                            pal = &s[i-tmp_minus..i+tmp_plus+1];
                            max = tmp_plus+1+tmp_minus
                        }
                        if char0 != char1 {
                            break
                        } else if i-tmp_minus == 0 {
                            break
                        } else {
                            tmp_minus += 1;
                            tmp_plus += 1;
                        }

                    }
                }
                
            }
            while i-minus >= 0 && i+plus < slen {
                let char0 = &s[i-minus..i-minus+1];
                let char1 = &s[i+plus..i+plus+1];
                if char0 == char1 && plus+1+minus > max {
                    pal = &s[i-minus..i+plus+1];
                    max = plus+1+minus;  
                }
                if char0 != char1 {
                    break
                } else if i-minus == 0 {
                    break
                } else {
                    minus += 1;
                    plus += 1;
                }   
            }
        }
        pal.to_string()
    }
}
