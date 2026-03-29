#Find all possible combinations that a string of integers that can be represented with their ascii counterparts
#Ex 1012 -> 10 1 2 -> J A B
    #or 10 12 JL
    #But not 1 01 2, because anything with zero infront isnt a valid ascii value
#At each step, we need to consider if we should consider the ith value as one valid digit, or conisder it and its
#Next digit as a valid letter
#If the current decoded part is >= 1  <= 26, then it is a valid part
#OTWS we cannot add the current value
#If we ever reach beyond the length of s, that tells us we completed a valid combination
class Solution:
    def numDecodings(self, s: str) -> int:
        res = []
        def dfs(i):
            if i >= len(s):
                return 1
            paths = 0
            
            #Two choices at each subproblem, we can either take the current digit as a single character
            #Or we can take the current digit and the next digit, if valid, and check the next character
            #If the current index can be a valid ascii value, add search its 
            #Decision Tree for a valid path
            
            #If this single character is a valid single character, check the amount of valid paths
            #From this character
            if s[i] != "0":
                paths += dfs(i+1)
            
            #If there atleast two characters we can take
            if i < len(s)-1:
                #Check if the combination of the ith character and its neighbour are a valid
                #Character, if they are, take it and explore the valid paths considering the pair
                #And the next character after it
                if ((s[i] == "1" and (s[i+1] >= "0" and s[i+1] <= "9")) or 
                    (s[i] == "2" and  s[i+1] < "7")):
                    paths += dfs(i+2)
            return paths
        

        cache = {}
        def memo(i):
            nonlocal cache
            if i >= len(s):
                return 1
            
            if i in cache:
                return cache[i]
            
            if s[i] != "0":
                cache[i] = cache.get(i, 0) + memo(i+1)

            if i < len(s)-1:
                if ((s[i] == "1" and (s[i+1] >= "0" and s[i+1] <= "9")) or 
                    (s[i] == "2" and  s[i+1] < "7")):
                    cache[i]= cache.get(i, 0) + memo(i+2)
            return cache[i] if i in cache else 0
        return memo(0) 
        


            

        