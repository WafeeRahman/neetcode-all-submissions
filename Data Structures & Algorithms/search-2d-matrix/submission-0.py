class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][0] > target:
                return False
            elif matrix[i][-1] < target:
                continue
            l = 0
            r = len(matrix[i]) -1
            mid = (l+r) // 2
            while l <= r:
                if matrix[i][mid] < target:
                    l = mid+1
                elif matrix[i][mid] > target:
                    r = mid-1
                else:
                    return True
                mid = (l+r) // 2
        return False