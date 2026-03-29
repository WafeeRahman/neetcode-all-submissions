#Given a list of string strs, return the longest ocmmon prefix of ALL strings
#This means that all strings must have a common prefix, and if we that one string among strs doesnt have it
# None of them do
# We can choose any of the strings in strs, and test against all of the strings for a prefix
# If the prefix does not match at all, return
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        #For each character in a common prefix between all strs
        for i in range(len(strs[0])):
            for string in strs:
                #If a string ends, or we find a mismatch, return the common prefix
                if i == len(string) or string[i] != strs[0][i]:
                    return res
            #If the current character of the prefix matches all strings, add it to res
            res += strs[0][i] 
        return res


        