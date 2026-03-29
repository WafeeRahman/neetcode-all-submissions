class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #Graph Nodes = Letters, Edges = Order starting that the greatest lex letter
        #Topsort so letters with the highest amt of incoming edges come first, reserse topsort for valid ordering
        adj = {}
        for word in words:
            for c in word:
                adj[c] = set()
        
        #Set ordering based on the first differing character of adjacent words
        print(len(words)-1)
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            minLen = min(len(word1), len(word2))
            
            #Invalid Ordering Check
            if len(word1) > len(word2) and word1[:minLen] == word2[:minLen]:
                return ""
                
            #Order characters by the first differing
            for j in range(minLen):
                #Word 1 Ordering at Char j > word 2 ordering
                if word1[j] != word2[j]:
                    adj[word1[j]].add(word2[j])
                    break
    
            #TopSort
        cycle = set()
        visit = set()
        alpha = []
        def dfs(node):
            if node in cycle:
                return False
            if node in visit:
                return True
            #Preorder Cycle Detection
            cycle.add(node)
            for nei in adj[node]:
                if nei in visit:
                    continue
                if not dfs(nei):
                    return False
            
            cycle.remove(node) #Backtrack
            visit.add(node)
            alpha.append(node) 
            return True

        for char in adj.keys():
            if not dfs(char):
                return ""

        alpha.reverse() #Reverse so that nodes w/ no indegrees come first
        return "".join(alpha) #join ordering into string
        
