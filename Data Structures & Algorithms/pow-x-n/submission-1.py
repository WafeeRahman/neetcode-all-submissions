#Given a floating point x and an integer value n, implement the function myPow, which calculates x raised to the power
#n, we cant use any builtins
class Solution:
    def myPow(self, x: float, n: int) -> float:

        #Exponentiate function
        res = 1
        for i in range(abs(n)):
            res = res * x
        if n < 0:
            return 1 / res
        return res

        