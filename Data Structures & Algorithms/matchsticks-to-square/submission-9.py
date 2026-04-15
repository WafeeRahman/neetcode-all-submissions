class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0:
            return False
        sideLength  = sum(matchsticks) // 4  
        used = set()
        def backtrack(i, curLen, sideCount):
            if sideCount == 4:
                return True
           
            if curLen == sideLength:
                return backtrack(0,0, sideCount+1)
                
            for j in range(i, len(matchsticks)):
                if j in used:
                    continue
                used.add(j)
                curLen += matchsticks[j]
                if backtrack(j+1, curLen, sideCount):
                    return True
                
                used.remove(j)
                curLen -= matchsticks[j]
            return False
                

                

                
        return backtrack(0, 0,0)
        