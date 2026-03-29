class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #[1,2,3,4,4] -> True
        #[1,2,3,4] -> False

        dupSet = set()
        for num in nums:
            if num in dupSet:
                return True
            dupSet.add(num)

        return False