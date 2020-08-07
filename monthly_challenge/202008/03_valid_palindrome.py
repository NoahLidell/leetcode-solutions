class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "":
            return True
        s = [c for c in s.lower() if c.isalnum()]
        for i in range(len(s)//2):
            if s[i] != s[(i+1)*-1]:
                return False
        return True
