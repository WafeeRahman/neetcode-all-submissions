class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        currNode = self.root
        for char in word:
            if char not in currNode.children:
                currNode.children[char] = TrieNode()
            currNode = currNode.children[char]
        currNode.word = True
    
    def search(self, word: str) -> bool:
        def dfs(i, root):
            if i == len(word):
                return root.word
            
            if word[i] != ".": 
                if not word[i] in root.children:
                    return False
                else:
                    return dfs(i+1, root.children[word[i]])
            
           
            for key in root.children.keys():
                if dfs(i+1, root.children[key]):
                    return True
            return False
            
           
        
        return dfs(0, self.root)
                     
       




       
       
            
            
            
            


        
