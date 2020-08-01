def detectCapitalUse(self, word: str) -> bool:
    all_caps = True
    all_lower = True
    first_caps = True
    for i, c in enumerate(word):
        all_caps = all_caps and c==c.upper()
        all_lower = all_lower and c!=c.upper()
        first_caps = first_caps and ((i==0) == (c==c.upper()))
    return all_caps or all_lower or first_caps
