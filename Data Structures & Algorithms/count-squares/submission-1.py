class CountSquares:

    def __init__(self):
        self.pointCount = {}
        self.points = []
        

    def add(self, point: List[int]) -> None:
        self.points.append(point)
        self.pointCount[tuple(point)] = self.pointCount.get(tuple(point), 0) + 1

    def count(self, point: List[int]) -> int:
        px, py = point
        res =0 
        for pt in self.points:
            x,y = pt
            #Take a diagonal point, and if the sidelengths of the height and length are equal, 
            #The height and length must be equal
            if (abs(px-x) != abs(py-y)) or x == px or y==py:
                continue
            else:
                #Check if there are two corresponding points to complete the squareA
                if (x,py) in self.pointCount and (px,y) in self.pointCount:
                    res += self.pointCount[(x,py)] * self.pointCount[(px,y)]
        return res


        
