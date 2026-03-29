class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        charSet = set()
        longest = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])  
                l+=1  
                   
            
            charSet.add(s[r])
            windowLen = r-l+1
            longest = max(windowLen, longest) 
        return longest


