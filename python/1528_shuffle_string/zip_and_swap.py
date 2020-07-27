class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        output = [None for _ in range(len(indices))]
        for c, i in zip(s, indices):
            output[i] = c
            
        return "".join(output)
