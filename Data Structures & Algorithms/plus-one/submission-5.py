class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        res = []
        base = len(digits)-1
        curSum = 0 
        for digit in digits:
            curSum = curSum + (digit* 10**base)
            base -= 1
        print(curSum)
        curSum += 1
        while curSum > 0:
            res.append(curSum % 10)
            curSum = curSum // 10
        res.reverse()
        return res