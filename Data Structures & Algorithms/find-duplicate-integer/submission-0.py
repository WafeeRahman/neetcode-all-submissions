class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Linked List Problem: Since we have n+1 integers within the range [1, n]
        #That tells us that each number in the array links to an index within the array
        #I.E [1,2,3,2,2] Index 0 Points to 2, 2 Points to 3, 3 Points to 2
        #If theres a duplicate, that would mean theres a cycle within the linked list

        slow = 0
        fast = 0 

        #We have the gurrantee that there WILL be a duplicate. Floyds Hare tells us that fast and slow will meet.
        while True:
            slow = nums[slow] #Traverse with linkages using fast and slow pointers
            #Traverse fast pointer twice as fast by continously referencing nums[fast] (the next linkage)
            fast = nums[nums[fast]]  
            if slow == fast:
                break
        slow2 = 0

        while True:
            slow2 = nums[slow2]
            slow = nums[slow]

            if slow == slow2:
                return slow
    