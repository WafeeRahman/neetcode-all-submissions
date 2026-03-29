#Given an array of nums containing n+1 integers, where each of the numbers range from 1-n
#Each number appears once except for one that appears twice
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Given that each number ranges from 1-n, that means that each value points to a different index in the array
        #Except 2 numbers that point to the same value, a cycle in a linked list. 
        #We can use floyd's tortoise algorithm to identify the cycle, and then use another slow pointer to 
        #Traverse to the point of the cycle

        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        
        while True:
            slow = nums[slow]
            slow2= nums[slow2]
            if slow == slow2:
                break
        return slow2
        