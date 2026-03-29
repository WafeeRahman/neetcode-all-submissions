class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        countMap = {}
        res = 0
        l = 0
        for r in range(len(s)):

            countMap[s[r]] = countMap.get(s[r], 0 ) + 1
            mostFreq = max(countMap, key=lambda x: countMap[x])
            windowLen = (r-l)+1
            
            
            if k >= (windowLen - countMap[mostFreq]):
                res = max(res, windowLen)
                print(l, r, countMap[mostFreq])
            
            
            while (windowLen - countMap[mostFreq]) > k:
                countMap[s[l]] -= 1
                l+=1
                windowLen = (r-l)+1
                mostFreq = max(countMap, key=lambda x: countMap[x])
                  
        return res
            
