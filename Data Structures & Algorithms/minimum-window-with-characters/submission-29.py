class Solution:
    def minWindow(self, s: str, t: str) -> str:
      
        countS = {}
        countT = {}
        windowRange =[-1,-1]
        res = float('inf')

        for i in range(len(t)):
            charT = t[i]
            countT[charT] = countT.get(charT, 0) + 1
        
        need = len(countT) #We need lent character count matches
        have = 0
        l=0

        for r in range(len(s)):
            countS[s[r]] = countS.get(s[r], 0) + 1
            
            if s[r] in countT and countS[s[r]] == countT[s[r]]:
                have += 1
            print(have, need)

            while have == need:
                windowLen=(r-l)+1
                
                if windowLen <= res:
                    res = windowLen
                    windowRange=[l, r]
                    
                
                countS[s[l]] -= 1
                
                if s[l] in countT and countS[s[l]] == countT[s[l]] -1:
                    have -=1
                
                l+=1
                
        return "" if res == float('inf') else s[windowRange[0]:windowRange[1]+1]



       

        
        