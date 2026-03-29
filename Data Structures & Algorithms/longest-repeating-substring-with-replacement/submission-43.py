class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = defaultdict(int)
        mostFreq = 0
        res = 0
        l = 0
        for r in range(len(s)):
            charCount[s[r]] += 1
            if charCount[s[r]] >= mostFreq:
                mostFreq = charCount[s[r]]
            
            windowLen = r-l+1
                
            while windowLen-mostFreq > k:
                charCount[s[l]] -=1 
                l+=1
                windowLen = r-l+1
            res = max(res, windowLen)
        return res
