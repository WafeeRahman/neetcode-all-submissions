class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)

        memoC = {}
        res = []
        def dfs(start):
            if start in memoC:
                return memoC[start]
            if start == len(s):
                return [""]
            lst = []
            for end in range(start+1, len(s)+1):
                if s[start:end] in wordSet:
                    word = s[start:end]

                    for retnVal in dfs(end):
                        if retnVal != "":
                            lst.append(word + " " + retnVal)
                        else:
                            lst.append(word + "")
            memoC[start]=lst

            return memoC[start]
        return dfs(0)