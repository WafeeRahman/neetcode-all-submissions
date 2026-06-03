class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for i in range(len(word)):
            char = word[i]
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
            if i == len(word)-1:
                cur.isEndOfWord=True
        
        

    def search(self, word: str) -> bool:
        cur = self.root
        if not word:
            return True
        
        def dfs(root, i):

            if not root:
                return False

            if i == len(word):
                return root.isEndOfWord

        
            if word[i] != "." and word[i] in root.children:
                return dfs(root.children[word[i]], i+1)
                

            if word[i] == ".":
                for child in root.children:
                    print(child)
                    if dfs(root.children[child], i+1):
                        return True
            return False 
        return dfs(self.root, 0)


        
