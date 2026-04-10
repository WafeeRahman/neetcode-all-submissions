class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []
        curComb = []
        combSet = set()
        def genComb(val):
            if tuple(curComb) in combSet:
                return
            if len(curComb) == k:
                res.append(curComb[:])
                combSet.add(tuple(curComb[:]))
                return
            if val > n:
                return
            curComb.append(val)
            genComb(val+1) 
            curComb.pop()
            genComb(val+1)
        
        genComb(1)
        return res