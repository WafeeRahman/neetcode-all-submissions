class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        countS = defaultdict(int)
        countT = defaultdict(int)


        for i in range(len(t)):
            countT[t[i]] += 1
        
        have = 0
        need = len(countT)

        l = 0
        res = [-1,-1]
        minWindowLen = float('inf')
        for r in range(len(s)):
            
            countS[s[r]] += 1
            if s[r] in countT:
                if countT[s[r]] == countS[s[r]]:
                    have += 1
            windowLen = r-l+1
            while have == need:
                if windowLen <= minWindowLen:
                    minWindowLen = windowLen
                    res = [l, r]
                countS[s[l]] -= 1
                if s[l] in countT:
                    if countS[s[l]] == countT[s[l]]-1:
                        have -= 1
                l+=1
                windowLen = r-l+1
        
        return s[res[0]:res[1]+1]
                    

