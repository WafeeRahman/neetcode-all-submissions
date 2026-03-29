class Solution:

    def encode(self, strs: List[str]) -> str:
        encodeSTR = ""
        for string in strs: 
            charCount = len(string)
            encodeSTR = encodeSTR + str(charCount)+"#" + string
            print(encodeSTR)
        return encodeSTR 

    def decode(self, s: str) -> List[str]:
        decodeLST = []
        i = 0 
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            i = j+1
            j = i+length
            decodeLST.append(s[i:j])
            i=j
        return decodeLST

        
