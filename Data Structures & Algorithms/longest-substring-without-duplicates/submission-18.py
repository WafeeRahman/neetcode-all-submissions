#with a string s, we need to find the longest substring where each character is unique
#where a substring is a contigous sequence of characters within a string
#In other words, we need to find the maximum contiguous window length where all characters in the string are unique
#We can track the current window of characters in a string, and take the maximum window length at each step, shrinking the window
#When we encounter duplicate values
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curCharSet = set() 
        longest = 1
        if len(s) == 0:
            return 0

        l = 0
        for r in range(len(s)):
            while s[r] in curCharSet:
                curCharSet.remove(s[l])
                l+= 1
                
            print(l, r, curCharSet)
            curCharSet.add(s[r])
            windowLen = (r-l)+1
            longest = max(windowLen, longest)
        return longest

         
