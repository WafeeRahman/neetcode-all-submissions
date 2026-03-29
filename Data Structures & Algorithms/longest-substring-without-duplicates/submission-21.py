class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        occured = set()
        l = 0
        res = float('-inf')
        for r in range(len(s)):
            while s[r] in occured:
                occured.remove(s[l])
                l+=1
            
            occured.add(s[r])
            resLen = (r-l)+1
            res = max(resLen, res)
        return res



