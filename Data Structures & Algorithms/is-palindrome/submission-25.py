class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Make lowercase and remove spaces
        sLower = s.lower() 
        sLower = sLower.replace(" ", "")

        #The Filter Function, filters a string by method and returns an object
        sLower = filter(str.isalnum, sLower) #Remove all symbols
        sLower = "".join(sLower)
        #Turn back into string using join function

        start = 0 
        end = len(sLower) - 1

        print(sLower)

        while start < end:
            #Base Case
            if sLower[start] != sLower[end]:
                return False
             #Continous Incrementation
            else: 
                start += 1
                end -= 1
                print(sLower[start], sLower[end])
        return True