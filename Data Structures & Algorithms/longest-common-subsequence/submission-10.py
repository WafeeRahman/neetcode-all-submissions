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
        #Bottom Up Dynamic Programming, start at the base case of the lengths building upon the previous result to get the max

        dpC= [[0] * (len(text2)+1) for _ in range(len(text1)+1)]
        def dp():
            for i in range(len(text1)-1, -1, -1):
                for j in range(len(text2)-1, -1, -1):
                    
                    if text1[i] == text2[j]:
                        #The cell diagonal should the built subsequence at i, j
                        dpC[i][j] = 1 + dpC[i+1][j+1]
                    else: 
                        #If we dont find a match, take the maximum subsequence length based on 
                        #traversing if we start from text1 (prev Column) vs text2(previous cell in same row)
                        dpC[i][j] = max(dpC[i+1][j], dpC[i][j+1])
            return dpC[0][0]
        return dp()


        
        