class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()

        slow, fast = nums[0], nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        slow2 = nums[0]

        while slow != slow2:
            slow2 = nums[slow2]
            slow = nums[slow]
        
        return slow

        