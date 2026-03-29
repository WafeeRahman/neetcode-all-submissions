class Solution:
    def longestPalindrome(self, s: str) -> str:
        #Bottom Up DP Solution
        #Start at the Subproblem, for each midpoint of a palindrome
        #(even and odd), expand left and right to see if it extends and take the maximum
        resLen = 0
        resIndex = 0
        for i in range(len(s)):

            #Odd Length, L==R Base Case
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l) >= resLen and s[l] == s[r]:
                    resLen = (r-l)+1
                    resIndex = l
                    
                #Expand Window
                l-=1
                r+=1
                
                            

            #Even Length Pal, no midpoint, l < r
            l = i
            r = i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l) >= resLen and s[l] == s[r]:
                    resLen = (r-l)+1
                    resIndex = l
                #Expand Window
                l-=1
                r+=1
                
                
        
        return s[resIndex:resIndex+resLen]

        