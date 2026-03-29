#Given two strings text 1 and text 2, return the length of the longest common subsequence between them
#If one exists, otws return zero
#A subsequence can be derived by the the common contigious order of values of the two strings at the same position
#But values inbetween common letters can be deleted

#IE cat and crabt
#c,a,t

#abcd, efgd, 1 d and d
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        #Recursive DFS

        def dfs(i,j):
            #If theres no possibility for a common value return zero
            if i == len(text1) or j == len(text2):
                return 0
            
            if text1[i] == text2[j]:
                return 1 + dfs(i+1,j+1) #If we find a common value, traverse to next comparison
            else:
                return max(dfs(i+1, j), dfs(i,j+1)) #Take the max subsequence between the decisions of continuing the sequence by
                #Traversing the first or second string
        
        #Optimize with a memoization cache
        #We know we have a result for each i and j, but can have the possibility of repeated calls
        #This gives us a 2D cache for each i and j + 1, as leni and lenj are guranteed zeroes as theyre no values at them
        #Make an mxn matrix for the letters of each text, and treat the indexes as such
        cache = [[-1] * len(text2) for _ in range(len(text1))]
        def memo(i,j):
            if i == len(text1) or j == len(text2):
                return 0
            
            if cache[i][j] != -1:
                return cache[i][j]
            
            if text1[i] == text2[j]:
                cache[i][j]= 1 + memo(i+1, j+1)
            else:
                cache[i][j]= max(memo(i+1,j), memo(i, j+1))
            return cache[i][j]
        return memo(0,0)

        
        