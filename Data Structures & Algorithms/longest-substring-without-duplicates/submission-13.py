class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding Window: Variable Size
        #Create a character set to store characters
        charSet = set()
        l=0 
        maxLen = 0
        for r in range(len(s)):
            #If we run into a duplicate, lets shrink our window
            while s[r] in charSet:
                charSet.remove(s[l]) #Remove whats at l
                l+=1  # Shrink window increment l
                
            #Add to charset and take maximum length
            charSet.add(s[r])
            maxLen = max(maxLen, (r - l + 1))
        return maxLen
        