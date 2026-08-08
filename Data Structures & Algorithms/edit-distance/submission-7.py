class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memoC = {}


        def memo(i,j):
            #Word Completed
            if i == len(word1):
                return len(word2) - j
            elif j == len(word2):
                return len(word1) - i
            elif (i,j) in memoC:
                return memoC[(i,j)]
            
            minOps = float('inf')
            #Character Mismatch, Do an Operation
            if i < len(word1) and j < len(word2) and word1[i] != word2[j]:
                #Replace
                minOps = min(minOps, 1+memo(i+1, j+1))
                #Delete
                minOps = min(minOps, 1+memo(i, j+1))
                #Insert
                minOps = min(minOps, 1+memo(i+1, j))
            #Character Match, No Operations
            elif i < len(word1) and j < len(word2) and word1[i] == word2[j]:
                minOps = min(minOps, memo(i+1, j+1))

               


            memoC[(i,j)] = minOps

            return memoC[(i,j)]

        return memo(0,0)
            
        