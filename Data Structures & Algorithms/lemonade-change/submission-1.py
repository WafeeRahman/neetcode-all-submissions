class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        total = 0
        billsCollected = {20:0, 10:0, 5:0}
        for bill in bills:
            if bill == 5:
                billsCollected[5] += 1
            elif bill == 20:
                if billsCollected[10] >= 1 and billsCollected[5] >= 1:
                    billsCollected[10] -= 1
                    billsCollected[5] -= 1
                elif billsCollected[5] >= 3:
                    billsCollected[5] -= 3
                else:
                    return False
            elif bill == 10:
                if billsCollected[5] >= 1:
                    billsCollected[5] -= 1
                    billsCollected[10] += 1
                else:
                    return False
            else:
                return False

        return True
        