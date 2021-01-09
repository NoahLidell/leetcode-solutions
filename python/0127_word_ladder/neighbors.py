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
        q = [(1, beginWord)]
        seen = set([beginWord])
        wlist = set(wordList)
        if endWord not in wlist:
            return 0

        def neighbors(word):
            from string import ascii_lowercase as alphabet

            word = list(word)
            neighbors = []
            for i in range(len(word)):
                for c in alphabet:
                    n = word[:]
                    n[i] = c
                    neighbors.append(n)
            return ["".join(n) for n in neighbors]

        while q:
            gen, w = q.pop(0)
            for n in neighbors(w):
                if n == endWord:
                    return gen + 1
                if n in wlist and n not in seen:
                    wlist.remove(n)
                    seen.add(n)
                    q.append((gen + 1, n))
        return 0
