#Given a list of words in lex order in an alien language, return the new lexical order of all characters in the wordset
#Identified by the ordering of certain letters in certain words vs others
#What we can do here is establish a graph of nodes with an edge u,v representing the lexical ordering of characters u, v relative
#To words, where u->v if u is less than v lexically, as per the words in words
#After establishing this graph, we can use topological sort to sort the characters based characters with no edges coming first
#(letters that are greatest in lexical order to least based on graph edges)
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        #Create AdjList, where graph
        for word in words:
            for char in word:
                adj[char] = set()

        for i in range(len(words)-1):
            minLen = min(len(words[i]), len(words[i+1]))
            word1 = words[i]
            word2 = words[i+1]
            if len(word1) > len(word2) and word1[:minLen] == word2[:minLen]:
                return ""
            for j in range(minLen):
                if word1[j] != word2[j]:
                    adj[word1[j]].add(word2[j])
                    break

        
        visit = set()
        cycle = set()
        alphabet = []
        def dfs(node):
            if node in cycle:
                return False
            if node in visit:
                return True
            
            cycle.add(node)
            for nei in adj[node]:
                if nei not in visit:
                    if not dfs(nei):
                        return False
            cycle.pop() 
            visit.add(node)
            alphabet.append(node)
            return True
            
        
        for char in adj.keys():
            if not dfs(char):
                return ""
        alphabet.reverse()
        return "".join(alphabet)
            

            
            
    


