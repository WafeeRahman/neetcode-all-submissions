class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        #We are looking for the maximum window length at which we can replace k characters
        charCount = {}
        l=0
        res = float("-infinity")
        for r in range(len(s)):
            #Count characters relative to our window.
            charCount[s[r]] = charCount.get(s[r], 0) + 1
            windowLen = r-l+1
            #Take the maximum character count in our window
            maxChar = max(charCount, key=charCount.get)
            #Window length - the maximum character that occurs = the amount of characters we can replace
            #If we can replace up to k characters within our window
            if windowLen - charCount[maxChar] <= k:
                res = max(res, windowLen)
            
            while windowLen - charCount[maxChar] > k:
                charCount[s[l]] -= 1
                l+= 1
                maxChar = max(charCount, key=charCount.get)
                windowLen = r-l+1 
        return res



        