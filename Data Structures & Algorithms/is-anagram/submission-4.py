class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        alphabet = [0] * 26

        for char in s:
            alphabet[ord(char) - ord('a')] += 1
        
        for char in t:
            alphabet[ord(char) - ord('a')] -= 1


        for count in alphabet:
            if count != 0:
                return False
        return True  
        
        