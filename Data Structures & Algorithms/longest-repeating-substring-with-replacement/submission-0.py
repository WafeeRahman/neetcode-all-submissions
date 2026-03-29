class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        charCount = {}
        res = 0
        charCount[0] = 0
        for R in range(len(s)):
            
            charCount[s[R]] = charCount.get(s[R], 0) + 1
            windowLen = R-L+1
            
            maxChar = max(charCount, key=lambda key: charCount[key]) if charCount else 0
            
            print(windowLen, charCount[maxChar], res, L, R)

            if windowLen - charCount[maxChar] <= k:
                res = max(res, windowLen)
            
            #Sliding Condition
            while windowLen - charCount[maxChar] > k:
                charCount[s[L]] -= 1 
                L+=1
                windowLen = R-L+1
                maxChar = max(charCount, key=lambda key: charCount[key])
            
            
        return res