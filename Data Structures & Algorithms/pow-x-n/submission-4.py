#Given a floating point x and an integer value n, implement the function myPow, which calculates x raised to the power
#n, we cant use any builtins
class Solution:
    def myPow(self, x: float, n: int) -> float:
       
        #Trivial Solution, multiply x by itself n times, if n is negative then the value is 1/x^n
        def exp(x,n):
            res = 1
            for i in range(abs(n)):
                res = res * x
            if n < 0:
                return 1 / res
            return res
        
        #What if instead of doing n calls, we could do n/2 calls for each exponent n, x^n/2 * x^n/2 = x^n
        def DivideAndConquer(x, n):
            if abs(n) == 0:
                return 1
            elif abs(n) == 1:
                return x
            elif x == 0:
                return 0
            
            if n % 2 == 1:
                return x * DivideAndConquer(x, n//2) * DivideAndConquer(x,n//2) 
            elif n % 2 == 0:
                return DivideAndConquer(x,n//2) * DivideAndConquer(x,n//2) 
        
        res = DivideAndConquer(x, abs(n))
        return res if n > 0 else 1/res
        
            

        