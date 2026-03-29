class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        #Count all Palindromic Substrings of even length and odd length
        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l-=1
                r+=1
                res+=1
            
            l = i 
            r = l+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l-=1
                r+=1
                res+=1
        
        return res



