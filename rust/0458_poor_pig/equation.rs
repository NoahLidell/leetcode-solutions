/*
458. Poor Pigs
Hard

There are 1000 buckets, one and only one of them is poisonous, while the rest are filled with water. They all look identical. If a pig drinks the poison it will die within 15 minutes. What is the minimum amount of pigs you need to figure out which bucket is poisonous within one hour?

Answer this question, and write an algorithm for the general case.

 

General case:

If there are n buckets and a pig drinking poison will die within m minutes, how many pigs (x) you need to figure out the poisonous bucket within p minutes? There is exactly one bucket with poison.

 

Note:

    A pig can be allowed to drink simultaneously on as many buckets as one would like, and the feeding takes no time.
    After a pig has instantly finished drinking buckets, there has to be a cool down time of m minutes. During this time, only observation is allowed and no feedings at all.
    Any given bucket can be sampled an infinite number of times (by an unlimited number of pigs).
*/
impl Solution {
    pub fn poor_pigs(buckets: i32, minutes_to_die: i32, minutes_to_test: i32) -> i32 {
        let mut x = 0i32;
        let T: i32 = minutes_to_test/minutes_to_die + 1;
        while T.pow(x as u32) < buckets {
            x += 1;
        }
        x
    }
}
