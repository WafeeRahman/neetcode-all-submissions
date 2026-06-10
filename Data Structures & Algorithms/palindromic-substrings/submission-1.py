class Solution:
    def countSubstrings(self, s: str) -> int:
        count=0
        for start in range(len(s)):

            l=r=start
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count+=1
                l-=1
                r+=1


    
            l=start
            r=start+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count+=1
                l-=1
                r+=1
        return count