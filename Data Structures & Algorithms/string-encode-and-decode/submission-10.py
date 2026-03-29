class Solution:

    def encode(self, strs: List[str]) -> str:
        newSTR = ""
        for string in strs:
            length = str(len(string))
            newSTR = newSTR + length + "#" + string
        print(newSTR)
        return newSTR


    def decode(self, s: str) -> List[str]:
        newList=[]
        i = 0
        while i < len(s):
            j=i
            while s[j] != "#":
                j+=1
            
            length=int(s[i:j])
            print(length)
            newList.append(s[j+1:j+length+1])
            i = j+length+1
        return newList

        
            

