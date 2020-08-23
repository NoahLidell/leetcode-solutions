"""
Stream of Characters

Implement the StreamChecker class as follows:

    StreamChecker(words): Constructor, init the data structure with the given words.
    query(letter): returns true if and only if for some k >= 1, the last k characters queried (in order from oldest to newest, including this letter just queried) spell one of the words in the given list.

 

Example:

StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // init the dictionary.
streamChecker.query('a');          // return false
streamChecker.query('b');          // return false
streamChecker.query('c');          // return false
streamChecker.query('d');          // return true, because 'cd' is in the wordlist
streamChecker.query('e');          // return false
streamChecker.query('f');          // return true, because 'f' is in the wordlist
streamChecker.query('g');          // return false
streamChecker.query('h');          // return false
streamChecker.query('i');          // return false
streamChecker.query('j');          // return false
streamChecker.query('k');          // return false
streamChecker.query('l');          // return true, because 'kl' is in the wordlist

 

Note:

    1 <= words.length <= 2000
    1 <= words[i].length <= 2000
    Words will only consist of lowercase English letters.
    Queries will only consist of lowercase English letters.
    The number of queries is at most 40000.

"""
class StreamChecker:
    def __init__(self, words: List[str]):
        trie = {}
        for word in words:
            head = trie
            for char in word:
                if char not in head:
                    head[char] = {}
                head = head[char]
            head['!'] = '!'
        self.trie = trie
        self.paths = []
        self.last = 'A'
                
    def query(self, letter: str) -> bool:
        paths = []
        if len(self.paths) == 2001:
            self.paths = self.paths[1:]
        if self.last and letter == self.last[-1]:
            self.last = self.last + letter
        if (letter != self.last and len(self.last) ==1) or (len(self.last) < 15):
            if head := self.trie.get(letter):
                paths.append(head)
        if self.last[-1] != letter:
            self.last = letter
        for path in self.paths:
            if len(path) > 2001:
                continue
            if continued := path.get(letter):
                paths.append(continued)
        self.paths = paths
        for path in self.paths:
            if path.get('!'):
                return True
        return False
                

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

