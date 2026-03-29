class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        #Our motivation: Find the smallest window length (substring) such that all character counts in window == t
        countT, window = {}, {}
        
        #Populate CounT
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        
        have = 0 
        need = len(countT)
        res, resLen = [-1,-1], len(s)
        #Need is the amount of matching counts we need between our window and T.
        
        #Once have == need, we have a valid substring.
        l=0
        for r in range(len(s)):
            
            c = s[r]
            window[c] = window.get(c, 0) + 1 
            if c in countT:
                if window[c] == countT[c]:
                    have += 1
            print (c, have, need)
            #Sliding Condition: Once we have a valid substring, we shrink our window to see if we can find a smaller window.
            while have == need:
                if (resLen >= (r-l+1)):  
                    resLen = (r-l+1)
                    res = [l, r]
                
                c = s[l]
                window[c] -= 1
                
                if c in countT:
                    if window[c] != countT[c]:
                        have -=1
                l += 1
        i, j = res[0], res[1]
        return s[i:j+1] if resLen != (float("infinity")) else ""
                
                
                



            
