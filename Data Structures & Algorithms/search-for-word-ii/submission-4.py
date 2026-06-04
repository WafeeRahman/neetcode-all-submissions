class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            cur = root
            for i in range(len(word)):
                char = word[i]
                if char not in cur.children:
                    cur.children[char] = TrieNode()
                cur = cur.children[char]
                if i == len(word)-1:
                    cur.isEnd = True
     
        res = []

        def dfs(r,c, cur, path, visit):
            if r>=len(board) or c >= len(board[0]) or min(r,c) < 0 or (r,c) in visit:
                return
            
            char = board[r][c]
            if char not in cur.children:
                return 
            visit.add((r,c))
            cur = cur.children[char]
            path.append(char)
            if cur.isEnd:
                res.append("".join(path))

            dfs(r+1,c,cur,path,visit)
            dfs(r-1,c,cur,path,visit)
            dfs(r, c-1,cur,path,visit)
            dfs(r, c+1,cur,path,visit)
            visit.remove((r,c))
            path.pop()
          
        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r,c,root,[], set())
        return list(set(res))