class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occurSet = set()
        maxLen = 0

        l = 0
        for r in range(len(s)):
            while s[r] in occurSet:
                occurSet.remove(s[l])
                l+=1
        
            occurSet.add(s[r])
            windowLen = r-l+1
            maxLen = max(windowLen, maxLen)
        return maxLen

        