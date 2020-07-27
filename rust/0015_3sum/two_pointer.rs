impl Solution {
    pub fn three_sum(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut triplets = Vec::new();
        let length = nums.len();
        if length < 3 {
            return triplets
        }
        let mut numbers = nums.clone();
        numbers.sort();

        for x in 0..length-2 {
            if x > 0 && numbers[x] == numbers[x-1] {
                continue
            }
            let mut left = x + 1;
            let mut right = length - 1;
            while left < right {
                let sum = numbers[x] + numbers[left] + numbers[right];
                if sum < 0 {
                    left += 1;
                } else if sum > 0 {
                    right -= 1;
                } else {
                    triplets.push(vec![numbers[x], numbers[left], numbers[right]]);
                    while numbers[left] == numbers[left + 1] && left < length - 2{
                        left += 1;
                    }
                    while numbers[right] == numbers[right - 1] && right > 1 {
                        right -= 1;
                    }
                    left += 1;
                    right -= 1;
                }
            }
        }
        triplets
    }
}

