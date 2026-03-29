class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        def dfs(i,j):
            #If we reach the end of word2, then the amount of operations required
            #Is the difference between the current ptr of word1 and its length
            if j == len(word2):
                return len(word1) - i
            #Same for Word1, if we're at the end of word1, without completing word2
            #Then the amount of ops left is the amount of ops we completed for j, and the total length of word2
            if i == len(word1):
                return len(word2) - j

            #Dont add an operation if the 
            if word1[i] == word2[j]:
                return dfs(i+1, j+1)
            
            else:
                insert = dfs(i, j+1)
                delete = dfs(i+1, j)
                replace = dfs(i+1,j+1)

                #Add One Operation to the Optimal Path
                return 1+ min(insert, replace, delete)
        
        memoC = {}

        def memo(i,j):
            #If we reach the end of word2, then the amount of operations required
            #Is the difference between the current ptr of word1 and its length
            
            if j == len(word2):
                return len(word1) - i
            
            #Same for Word1, if we're at the end of word1, without completing word2
            #Then the amount of ops left is the amount of ops we completed for j, and the total length of word2
            if i == len(word1):
                return len(word2) - j
            
            #Return Cache Lookups
            if (i,j) in memoC:
                return memoC[(i,j)]
            
            if word1[i] == word2[j]:
                memoC[(i,j)] = memo(i+1, j+1)
            
            else:
                insert = memo(i, j+1)
                delete = memo(i+1, j)
                replace = memo(i+1,j+1)

                #Add One Operation to the Optimal Path
                memoC[(i,j)] =  1+ min(insert, replace, delete)
            
         
        
        
        def dp():
            cache = [ [float('inf')] * (len(word2)+1) for _ in range(len(word1) + 1)]
            #Setup Base Cases
            for j in range(len(word2)+1):
                cache[len(word1)][j] = len(word2) - j
            for i in range(len(word1)+1):
                cache[i][len(word2)] = len(word1) - i 
            
            for i in range(len(word1)-1, -1, -1):
                for j in range(len(word2)-1,-1,-1):

                    if word1[i] == word2[j]:
                        cache[i][j] = cache[i+1][j+1]
                    else:
                        insert = cache[i][j+1]
                        delete = cache[i+1][j]
                        replace = cache[i+1][j+1]
                        cache[i][j] = 1 + min(insert, delete, replace)
            return cache[0][0]
        return dp()


           
    