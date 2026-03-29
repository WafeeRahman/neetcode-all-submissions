class DSU:
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(n+1):
            self.par[i] = i
            self.rank[i] = 0
    
    def find(self, n):
        if n != self.par[n]:
            self.par[n] = self.find(self.par[n])
        return self.par[n]

    def union(self, p1, p2):
        p1, p2 = self.find(p1), self.find(p2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        count = 0
        for u, v in edges:
            if dsu.union(u,v):
                count+=1
        return n-count
              
