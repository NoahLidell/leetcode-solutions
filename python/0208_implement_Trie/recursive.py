def recursive_insert(leaf, word):
    if len(word) > 1:
        first = word[0]
        next_leaf = leaf.setdefault(first, {})
        recursive_insert(next_leaf, word[1:])
    else:
        final = leaf.setdefault(word[0], {}) 
        final["END"] = True
        
def recursive_search(path, word):
    if len(word) > 1:
        first, rest = word[0], word[1:]
        try:
            return recursive_search(path[first], rest)
        except KeyError:
            return False
    else:
        try:
            return path[word[0]].get("END")
        except KeyError:
            return False
def recursive_starts_with(path, word):
    if len(word) > 1:
        first, rest = word[0], word[1:]
        try:
            return recursive_starts_with(path[first], rest)
        except KeyError:
            return False
    else:
        return path.get(word)

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tree = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        return recursive_insert(self.tree, word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return recursive_search(self.tree, word)

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return recursive_starts_with(self.tree, prefix)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
