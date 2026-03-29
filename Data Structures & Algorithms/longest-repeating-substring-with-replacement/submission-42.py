class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = defaultdict(int)
        mostFreq = 0
        res = 0
        l = 0
        for r in range(len(s)):
          
            charCount[s[r]] += 1
            mostFreq = max(charCount.values())
            
            
            windowLen = r-l+1

            if (windowLen-mostFreq) <= k:
                print(l, r, s[l:r+1], charCount, mostFreq, windowLen)
                res = max(res, windowLen)
            
            while windowLen-mostFreq > k:
                charCount[s[l]] -=1 
                l+=1
                mostFreq = max(charCount.values())
                windowLen = r-l+1
      
        return res
