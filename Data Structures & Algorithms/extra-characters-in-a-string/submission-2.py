class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        root = TrieNode()
        for word in dictionary:
            cur = root
            for i in range(len(word)):
                char = word[i]
                if char not in cur.children:
                    cur.children[char] = TrieNode()
                cur = cur.children[char]
                if i == len(word)-1:
                    cur.isEnd = True
        memo = {}
        def dfs(i, root):
            if i in memo:
                return memo[i]
            if i == len(s):
                return 0
            

            best = 1 + dfs(i+1, root)
            cur = root
            for j in range(i, len(s)):
                char = s[j]
                if not char in cur.children:
                    break
                cur = cur.children[char]
                if cur.isEnd:
                    best = min(best, dfs(j+1, root))

            

            memo[i] = best
            return memo[i]
        return dfs(0,root)