class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 0
        R = len(numbers) -1 

        while L < R:
            #If our Largest number plus our Smallest number is greater than our target, then our largest number isnt the sol
            if numbers[L]+numbers[R] > target:
                R -= 1
            #Vice Versa.
            elif numbers[L]+numbers[R] < target:
                L += 1
            else:
                return [L+1, R+1]
        return False