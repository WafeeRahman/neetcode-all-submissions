class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for string in strs:
            res.append(str(len(string)) + "#" + string)
        print(''.join(res))
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        i = 0 
        res = []

        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            i=j+1 #First Letter
            j=i+length #Move to Next Number
            res.append(s[i:j])
            i=j #Next Value for next Iteration
        
        return res
        
