class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n 
        fast = n

        
        def digitSum(num):
            digSum = 0
            while num > 0:
                digSum += (num % 10)**2
                num = num // 10
            return digSum

        slow = n
        fast = digitSum(n)
     
        while fast != 1:
            slow = digitSum(slow)
            fast = digitSum(digitSum(fast))
            if slow == fast:
                return False
        return True
    
        