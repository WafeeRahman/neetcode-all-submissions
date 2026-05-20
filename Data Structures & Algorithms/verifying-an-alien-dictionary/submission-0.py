class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        adj = {}
        for i in range(len(order)):
            char = order[i]
            adj[char] = i
        

        for i in range(len(words)-1):
            minlen = min(len(words[i]), len(words[i+1]))
            
            j = 0
            k = 0
            broke = False
            while j < minlen and k < minlen:
                if adj[words[i][j]] < adj[words[i+1][k]]:
                    broke = True
                    break
                elif adj[words[i][j]] > adj[words[i+1][k]]:
                    print(words[i][j]) 
                    print(words[i+1][k])
                    return False
                j+=1
                k+=1
            if len(words[i]) > len(words[i+1]) and not broke:
                return False
            continue
        return True



        
       