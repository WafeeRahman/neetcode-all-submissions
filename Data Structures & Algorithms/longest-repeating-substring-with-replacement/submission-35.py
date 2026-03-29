class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l=0
        charCount = [0] * 26
        res = 0
        for r in range(len(s)):
            charCount[ord(s[r]) - ord('A')] += 1
            maxFreq = max(charCount)
            windowLen = (r-l)+1

            if (windowLen - maxFreq) <= k:
                res = max(res, windowLen)
               
            
            while  (windowLen - maxFreq) > k:
                charCount[ord(s[l]) - ord('A')] -= 1
                l+=1
                maxFreq = max(charCount)
                windowLen = (r-l)+1

        return res



            