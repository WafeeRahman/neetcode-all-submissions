#Given a string s, split the string into as many substrings as it takes where each letter in the substring
#Appears only in the substring, and not in any substrings that comprize of s

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = [0]*26
        l=0
        r=len(s)-1
        #Select a substring x such that all appearences of x are contained within x (feasible)
        #If any other letters can be apart of this substring (last index of y <= x)
        #If there is a character within the substring that has a greater last index, we must extend the substring
        
        #Keep track of last indexes
        for i in range(len(s)):
            lastIndex[ord(s[i]) - ord('a')] = i

        maxLast = float('-inf')
        res = []
        l = 0
        for r in range(len(s)): 
            
            if lastIndex[ord(s[r]) - ord('a')] >= maxLast:
                maxLast = lastIndex[ord(s[r]) - ord('a')]
            
            if r == maxLast:
                size = (r-l)+1
                res.append(size)
                l=r+1
                print(s[r], maxLast)
               
              
        return res

          

        