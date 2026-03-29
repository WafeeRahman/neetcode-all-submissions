class TrieNode():
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        currNode = self.root
        for char in word:
            if char not in currNode.children:
                currNode.children[char] = TrieNode()
            currNode = currNode.children[char]
        currNode.isEndOfWord = True

        

    def search(self, word: str) -> bool:
        def dfs(i, root):
            if i == len(word):
                return root.isEndOfWord
            
            if word[i] == ".":
                for child in root.children.keys():
                    if dfs(i+1, root.children[child]):
                        return True
                return False
            if not word[i] in root.children:
                return False
            else:  
                return dfs(i+1, root.children[word[i]])    
        
        return dfs(0, self.root)
        
        
