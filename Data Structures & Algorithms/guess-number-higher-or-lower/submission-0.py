# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l=1
        r=n

        while l<=r:
            
            guessedVal = (l+r)//2
            theGuess = guess(guessedVal)
            if theGuess == 1:
                l=guessedVal+1
            elif theGuess == -1:
                r=guessedVal-1
            else:
                return guessedVal
        return guessedVal




        