class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLen = float('-inf')
        for start in range(len(s)):
            

            l = r = start
            curLen = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curLen = r-l+1
                if curLen >= maxLen:
                    maxL = l
                    maxR = r
                    maxLen = max(maxLen, curLen)
                    print(s[l:r+1])
                l-=1
                r+=1
            
        
            curLen = 0
            l=start
            r=start+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curLen = r-l+1
                if curLen >= maxLen:
                    maxL = l
                    maxR = r
                    maxLen = max(maxLen, curLen)
                l-=1
                r+=1
        if not maxLen:
            return s[0]
        return s[maxL:maxR+1]