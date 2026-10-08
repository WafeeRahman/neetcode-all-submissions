class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    

        l=0
        r=len(matrix)-1

        while l<=r:
            mid = (l+r)//2
            if target > matrix[mid][-1]:
                l=mid+1
            elif target < matrix[mid][0]:
                r=mid-1
            else:
                break
    
   
        mid = (l+r)//2
        l = 0 
        r = len(matrix[mid])-1
        while l<=r:
            mid2 = (l+r)//2
            if matrix[mid][mid2] > target:
                r = mid2-1
            elif matrix[mid][mid2] < target:
                l= mid2+1
            else:
                return True
        return False

