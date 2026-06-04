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
                    cur.children[char]=TrieNode()
                cur = cur.children[char]
                if i == len(word)-1:
                    cur.isEnd = True
        
        memo = {}
        n=len(s)
        def dfs(i):
            if i >= len(s):
                return 0
            if i in memo:
                return memo[i]

            best = 1 + dfs(i+1)
            cur = root
            for j in range(i, n):
                char = s[j]
                if char not in cur.children:
                    break
                cur = cur.children[char]
                if cur.isEnd:
                    best = min(best, dfs(j+1))
            memo[i]=best
            return memo[i]
        return dfs(0)
            


        