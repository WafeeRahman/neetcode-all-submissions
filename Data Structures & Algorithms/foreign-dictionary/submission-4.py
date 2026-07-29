class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        for word in words:
            for char in word:
                adj[char] = []
        for i in range(len(words)-1):
            next = words[i+1]
            minLen = min(len(words[i]), len(words[i+1]))

            if len(words[i]) != minLen == len(words[i+1]) and words[i][:minLen] == words[i+1]:
                return ""

            for j in range(minLen):
                if words[i][j] != words[i+1][j]:
                    adj[words[i][j]].append(words[i+1][j])
                    break
        

        visit = set()
        cycle = set()
        res = []


        def dfs(node):

            if node in cycle:
                return False

            if node in visit:
                return True
                 
            visit.add(node)     
            cycle.add(node)
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            cycle.remove(node)
       
            res.append(node)
            return True
        
        for char in adj:
            if char not in visit:
                if not dfs(char):
                    return ""
        return ''.join(res[::-1])