class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        temp = ""

        for i in range(len(s)):
            if i >len(s)-1-i:
                break
            temp = s[i]
            s[i] = s[len(s)-1-i]
            s[len(s)-1-i] = temp
        
            
       
        