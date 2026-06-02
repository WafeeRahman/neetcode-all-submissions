class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class PrefixTree:

    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for i in range(len(word)):
            char = word[i]
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
            if i == len(word)-1:
                cur.isEnd = True

    def search(self, word: str) -> bool:

        cur = self.root
        for i in range(len(word)):
            char = word[i]
            if char not in cur.children:
                return False
            else:
                cur = cur.children[char]
        return cur.isEnd

        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for i in range(len(prefix)):
            char = prefix[i]
            if char not in cur.children:
                return False
            else:
                cur = cur.children[char]
        return True

        