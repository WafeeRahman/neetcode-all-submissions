#Given two strings t1 and t2, find the length of the longest common subsequence if one exists
#OTWS return zero
#For any two strings, a subsequence is a sequence that can be made from deleting some or no elements while maintaining relative
#Order of the characters
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        #We can use recursion to check each character match, and return the max of whether we choose to progress
        #The subsquence at t1 or t2
        #Make sure to stop when either of them reach out of bounds
        def recursive(i,j):
            t1 = text1
            t2 = text2
            if i == len(t1) or j == len(t2):
                return 0
            if t1[i] == t2[j]:
                #Add one to the longest length subsequence when choosing to progress either string
                return 1 + recursive(i+1,j+1)
            else:
                #Dont add one when theres no match
                return max(recursive(i+1,j), recursive(i,j+1))

        #Initialize Memoization Cache for Repeated Calls
        cache = [[-1] * len(text1) for _ in range (len(text2))] 
        def memo(i, j):
            if i == len(text2) or j == len(text1):
                return 0
            
            elif cache[i][j] != -1:
                return cache[i][j]
            
            if text2[i] == text1[j]:
                cache[i][j] = 1 + memo(i+1,j+1)
            
            else:
                cache[i][j] = max(memo(i+1, j), memo(i,j+1))
            
            return cache[i][j]
        return memo(0,0)

    