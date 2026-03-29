class Solution:
    def mySqrt(self, x: int) -> int:

        if x == 1:
            return 1
        if x == 0:
            return 0
  
        l = 1
        r = x // 2


        while l <= r:

            mid = (l+r)//2

            if mid*mid < x:
                l = mid+1
            elif mid*mid > x:
                r = mid-1
            else:
                print(l,r,mid)
                return mid
  
        return r


        