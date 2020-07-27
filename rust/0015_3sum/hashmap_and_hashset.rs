use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn three_sum(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut count: HashMap<i32, i32> = HashMap::new();
        let mut block: HashSet<(i32, i32)> = HashSet::new();
        let mut triplets = Vec::new();
        for n in nums.clone() {
            *count.entry(n).or_insert(0) += 1
        }
        //println!("{:?}", count);
        
        let length = &nums.len();
        for i in 0..*length {
            for j in i+1..*length {
                
                let x = nums[i];
                let y = nums[j];
                if block.contains(&(x,y)) == false {
                    let z = 0 - (x + y);
                    let mut check = 0;
                    if z == x || z == y {
                        check = 1;
                    }
                    if x == 0 && y == 0 {
                        check = 2;
                    }
                    match count.get(&z) {
                        Some(&number) if number - check > 0 => {
                            //println!("{} {}", &z, &number);
                            triplets.push(vec![x, y, z]);
                            block.insert((x,y));
                            block.insert((y,x));
                            block.insert((y,z));
                            block.insert((z,y));
                            block.insert((x,z));
                            block.insert((z,x));
                        }
                        _ => {}
                    }
                } 
            }
        }

        triplets
    }
}
