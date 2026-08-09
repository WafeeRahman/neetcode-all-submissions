class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            j=i
            count =0
            while j>0:
                if j & 1 == 1:
                    count += 1
                j = j>>1
            res.append(count)
        return res
