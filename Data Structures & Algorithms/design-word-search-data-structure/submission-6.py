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
        #Use Recursive Backtracking to check possibilites for "."
        def dfs(i, root):
            #If we incremented i to the length of word, 
            #That tells us we traversed to the word
            if i == len(word):
                return root.word 
            
            #If the word is not "."
            if word[i] != ".": 
                #If the word is not available under searching the current roots children
                if not word[i] in root.children:
                    return False
                else:
                    #Increment I pointer, looking under the children of the current root
                    #To traverse to the end of the word
                    return dfs(i+1, root.children[word[i]])
            
            #Exhaust backtracking by iterating through all the current possible
            #Children in trie node that can fill in for "."
            for key in root.children.keys():
                #If any of them are valid, return true
                if dfs(i+1, root.children[key]):
                    return True
            return False #OTWS return False
            
        return dfs(0, self.root)
                     
       




       
       
            
            
            
            


        
