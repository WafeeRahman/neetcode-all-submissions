class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for word in strs:
            res = res + str(len(word)) + "#" + word
        
        print(res)
        return res


    def decode(self, s: str) -> List[str]:
        
        res = []
        i, j = 0, 0

        while i < len(s):
            while s[j].isdigit():
                j += 1
            length = int(s[i:j])
            i = j+1 
            res.append(s[i:i+length])
            i = i +length
            j = i
        return res

            