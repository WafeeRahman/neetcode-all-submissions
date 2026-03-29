class DSU:
    def __init__(self, n):
        self.par = {}
        self.rank = {}
        
        #To start each parent of a node is itself
        #Rank is zero as none are connected yet
        for i in range(n+1):
            self.par[i] = i
            self.rank[i] = 0
    
    def find(self, n):
        #If this node isnt the highest parent (where parent is the same as itself)
        if n != self.par[n]:
            #Recursively set the parent of the node to the parent of the highest parent
            #To decrease lookup time
            self.par[n] = self.find(self.par[n])
        return self.par[n] #Return Root/Parent

    def union(self, p1, p2):
        p1, p2 = self.find(p1), self.find(p2)
        if p1 == p2:
            return False
        #Set Parents based on height/rank
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
        #Originall the amount of components will be the verticies, 
        #as the graph has no edges
        #Union verticies as we build the graph
        for u, v in edges:
            #For each union where the parents arent common (noncyclic)
            if dsu.union(u,v):
                #Increment the amount of components
                count+=1
        #The amount of connected components should be n- union finds called
        return n-count
              
