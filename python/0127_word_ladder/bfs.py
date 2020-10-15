"""
127. Word Ladder
Medium

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

    Only one letter can be changed at a time.
    Each transformed word must exist in the word list.

Note:

    Return 0 if there is no such transformation sequence.
    All words have the same length.
    All words contain only lowercase alphabetic characters.
    You may assume no duplicates in the word list.
    You may assume beginWord and endWord are non-empty and are not the same.

Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
	
https://leetcode.com/problems/word-ladder/
"""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import deque, defaultdict
        trans = defaultdict(list)
        L = len(beginWord)
        if endWord not in wordList:
            return 0
        words = [beginWord] + wordList
        for w in words:
            for i in range(L):
                inter = w[:i]+"*"+w[i+1:]
                trans[inter].append(w)
        queue = deque([(beginWord,1)])
        while queue:
            word, lvl = queue.popleft()
            for i in range(L):
                inter = word[:i]+"*"+word[i+1:]
                
                for w in trans[inter]:
                    if w == endWord:
                        return lvl + 1
                    queue.append((w, lvl+1))
                    
                trans[inter] = []
        return 0
        
