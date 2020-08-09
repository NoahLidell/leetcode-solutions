class Solution:
    def isValid(self, s: str) -> bool:
        def fail_bc_negative(self) -> bool:
            if self.parentheses < 0 or self.curly_bracket < 0 or self.angle_bracket < 0:
                return True
            else:
                return False
        def adjust(self, char: str) -> None:
            if char == "(":
                self.parentheses += 1
            elif char == ")":
                self.parentheses -= 1
            elif char == "[":
                self.angle_bracket += 1
            elif char == "]":
                self.angle_bracket -= 1
            elif char == "{":
                self.curly_bracket += 1
            elif char == "}":
                self.curly_bracket -= 1
            #print(self.parentheses, self.angle_bracket, self.curly_bracket)
        opens = set(["[", "{", "("])
        closes = set(["]", "}", ")"])
        pairs = {"(":")", "[":"]", "{":"}"}
        self.parentheses = 0
        self.angle_bracket = 0
        self.curly_bracket = 0
        prev_open = []
        for i, c in enumerate(s):
            adjust(self, c)
            if prev_open != [] and c in closes:
                if pairs[prev_open.pop()] != c:
                    #print(f"{i} {c} does not match prev open {prev_open}")
                    return False
            if c in opens:
                #print(f"{i} set prev to {c}")
                prev_open.append(c)
            if fail_bc_negative(self):
                #print(f"{i}, {c}, {s}: fail bc negative")
                #print(self.parentheses, self.angle_bracket, self.curly_bracket)
                return False
        if prev_open == []:
            return True
        else:
            return False
