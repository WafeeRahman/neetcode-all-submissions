class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        cur = 0
        while cur != slow:
            cur = nums[cur]
            slow = nums[slow]

        return cur

        