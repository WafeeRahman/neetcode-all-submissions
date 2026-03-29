class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        charCount = {}
        res = 0
        charCount[0] = 0

        #Sliding Window: Take the largest frequent character within our window and the
        #Window Length, if their difference is <= to k, then we can replace characters and 
        #Have a windowLen substring of repeated characters
        for R in range(len(s)):
            
            #Increment charCount hash
            charCount[s[R]] = charCount.get(s[R], 0) + 1
            #Take WindowLen and MaxChar key
            windowLen = R-L+1
            
            maxChar = max(charCount, key=lambda key: charCount[key]) if charCount else 0
            
            #print(windowLen, charCount[maxChar], res, L, R)

            #Condition that we change Res
            if windowLen - charCount[maxChar] <= k:
                res = max(res, windowLen)
            
            #Sliding Condition, if our string is invalid, slide l until it isnt, change things
            #Accordingly
            while windowLen - charCount[maxChar] > k:
                charCount[s[L]] -= 1 
                L+=1
                windowLen = R-L+1
                maxChar = max(charCount, key=lambda key: charCount[key])
            
        #Return the max window length that is valid    
        return res