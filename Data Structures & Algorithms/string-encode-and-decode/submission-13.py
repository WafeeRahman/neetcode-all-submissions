class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            length = str(len(string))
            res += length +"#" +string

        print(res)
        return res

    def decode(self, s: str) -> List[str]:

        i = 0
        j = 0
        res = []
        while i < len(s):
            j=i
            while s[j] != "#" and j < len(s):
                j+=1
            print(s[i], s[j])
            length = int(s[i:j])
            i = j+1
            
            word = s[i:i+length]
            res.append(word)
            
            i=i+length

        return res
        