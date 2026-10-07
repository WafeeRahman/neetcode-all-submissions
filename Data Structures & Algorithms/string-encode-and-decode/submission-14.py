class Solution:

    def encode(self, strs: List[str]) -> str:
        newS = ""
        for word in strs:
            length = len(word)
            newS += str(length) + "#" + word
        return newS


    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        j = 0

        while i < len(s):
            if s[i].isdigit():
                j=i
                while s[j] != "#":
                    j+=1
            length = int(s[i:j])
            i = j+1
           
            res.append(s[i:i+length])
            i = i+length
        return res
