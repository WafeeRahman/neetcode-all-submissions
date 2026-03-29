class Solution:
    def validPalindrome(self, s: str) -> bool:
        


        def isPal(l, r):

            while l<=r:

                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True
        

        count = 0 


        l=0
        r=len(s)-1


        while l<=r:
            if s[l] != s[r]:
                if isPal(l+1, r):
                    return True
                if isPal(l, r-1):
                    return True
                else:
                    return False
            l+=1
            r-=1
        return True