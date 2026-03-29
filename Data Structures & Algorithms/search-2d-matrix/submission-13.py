class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])


        nums = matrix
        l = 0
        r = ROWS-1

        while l <= r:
            mid= (r+l)//2

            if nums[mid][0] > target:
                r = mid-1
            elif nums[mid][-1] < target:
                l = mid+1
            else:
                break
        
        l=0
        r=COLS-1

        while l <= r:
            midC = (r+l)//2
            if nums[mid][midC] > target:
                r = midC-1
            elif nums[mid][midC] < target:
                l = midC+1
            else:
                return True
        return False
         