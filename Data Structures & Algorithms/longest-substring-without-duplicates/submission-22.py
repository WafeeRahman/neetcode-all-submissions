class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occuredSet = set()
        l = 0
        maxWindow = 0
        for r in range(len(s)):
            while s[r] in occuredSet:
                occuredSet.remove(s[l])
                l+=1
            windowLen = (r-l)+1
            maxWindow=max(windowLen, maxWindow)
            occuredSet.add(s[r])
        return maxWindow




        