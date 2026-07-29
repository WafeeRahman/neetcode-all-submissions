class UnionFind:

    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(n+1):
            self.par[i] = i
            self.rank[i] = 0
    
    def find(self, node):
        if node != self.par[node]:
            self.par[node] = self.find(self.par[node])
        return self.par[node]
    
    def union(self, node1, node2):
        p1, p2 = self.find(node1), self.find(node2)

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
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        i = 0
        for edge in edges:
            edge.append(i)
            i+=1

   
        def kruskal(n, exclude=-1, include=-1):
            minHeap = []
            for ai, bi, w, i in edges:
                if i == exclude or i == include:
                    continue
                heapq.heappush(minHeap, (w, ai, bi, i))
            
            unionFind = UnionFind(n)
            mst = []
            weightSum = 0
            if include != -1:
                ai, bi, wi, i = edges[include]
                unionFind.union(ai, bi)
                mst.append((ai, bi))
                weightSum += wi

            while minHeap and len(mst) < n-1:
                weight, ai, bi, i = heapq.heappop(minHeap)
                if i == exclude or i == include:
                    continue
           
                if not unionFind.union(ai, bi):
                    continue
                weightSum += weight
                mst.append((ai, bi))
            
            return weightSum if len(mst) == n-1 else float('inf')
        
        base = kruskal(n)
        critical = []
        psuedo = []

        for i in range(len(edges)):
            if kruskal(n, i) > base:
                critical.append(i)
            elif kruskal(n,-1,i) == base:
                psuedo.append(i)
        res = []
        res.append(critical)
        res.append(psuedo)
        return res

     
        