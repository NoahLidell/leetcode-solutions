def abs(n):
    if n < 0:
        return n*-1
    else:
        return n

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0

        if len(arr) < 3:
            return count
        x = arr[0]
        for i in range(0, len(arr)-2):
            for j in range(i+1, len(arr)-1):
                x = arr[i]
                y = arr[j]
                if abs(x - y) <= a:
                    for k in range(j+1, len(arr)):
                        z = arr[k]
                        if abs(y -z) <= b and abs(x-z) <= c:
                            count += 1
                else:
                    continue
        return count
