#Given an mxn matrix of integers, return the list in spiral order
#Starting top left to top right, top right to bottom right at the final column, bottom right to bottom left
#and then bottom left to top right, 1 cell under where we started
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        ROWS = len(matrix)
        COLS = len(matrix[0])
        visit = set()
        top = 0
        bottom = ROWS-1
        left = 0
        right = COLS-1
        res = []
        while top <= bottom and left <= right:
            #Traverse top left to top right
            for i in range(left, right+1):
                print(matrix[top][i])
                res.append(matrix[top][i])
            top += 1
            
            #Traverse top right (next cell after top right) to bottom right
            for i in range(top, bottom+1):
                print(matrix[i][right])
                res.append(matrix[i][right])
            right -= 1
            
            if not (left <= right and top <= bottom):
                break
      
            #Traverse bottom right to bottom left
            for i in range(right, left-1,-1):
                print(matrix[bottom][i])
                res.append(matrix[bottom][i])
            bottom -= 1
            
            #Traverse bottom left to top left
            for i in range(bottom, top-1, -1):
                res.append(matrix[i][left])
            left +=1
           
        return res







        