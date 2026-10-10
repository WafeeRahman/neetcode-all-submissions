class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countS = defaultdict(int)
        countT = defaultdict(int)

        for i in range(len(t)):
            countT[t[i]] += 1

        have = 0
        need = len(countT)
        minWindowLen = float('inf')
        minWindow = [-1, -1]
        l = 0
        for r in range(len(s)):
            
            countS[s[r]] +=1
            if countS[s[r]] ==  countT[s[r]]:
                have += 1
            
            while have == need:
                if minWindowLen > r-l+1:
                    minWindowLen = r-l+1
                    minWindow = [l,r]
                countS[s[l]] -= 1
                if countS[s[l]] < countT[s[l]]:
                    have -=1 
                l+=1
        if minWindow == [-1, -1]:
            return ""
        return s[minWindow[0]:minWindow[1]+1]
    
    



