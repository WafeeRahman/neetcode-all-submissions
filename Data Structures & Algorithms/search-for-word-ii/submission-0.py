class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        currNode = self.root
        for char in word:
            if not char in currNode.children:
                currNode.children[char] = TrieNode()
            currNode = currNode.children[char]
        currNode.word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        prefixTrie = Trie()
        for word in words:
            prefixTrie.addWord(word)
        path = set()
        res = []
        def dfs(r, c, i, word, currNode):
            nonlocal res
            if currNode.word:
                res.append(word)
                return 
               
            if (min(r,c) < 0 
               or r >= len(board) 
               or c >= len(board[0]) 
               or i > len(word) 
               or board[r][c] != word[i]
               or (r,c) in path
               or word[i] not in currNode.children):
                return 
            
            currNode = currNode.children[word[i]]
            path.add((r,c))
            
            i+=1

            dfs(r+1, c, i, word, currNode) 
            dfs(r-1, c, i, word, currNode) 
            dfs(r,c+1,i, word, currNode) 
            dfs(r,c-1,i, word, currNode)
            
            path.remove((r,c))

            return
        
        for word in words:
            for r in range(len(board)):
                for c in range(len(board[0])):

                    dfs(r,c,0,word,prefixTrie.root)
        return list(set(res))
     
        