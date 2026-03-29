#Given an 2d array of points where each value is a 2-tuple that represents a point xi, yi
#The cost of connecting any two points on the graph is |xi - xj| + |yi - yj| 
#We need to return the minimum cost of connecting the points together, where there is only one path
#Between each point (no cycles)

#To do this, we can construct an adjacency list w/ the original points and convert it into an MST
#Getting the minimum cost to connect each point

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjList = {}
        for i in range(len(points)):
            adjList[i] = []
        
        for i in range(len(points)):
            xi, yi = points[i]
            
            for j in range(i+1, len(points)):
                xj, yj = points[j]
                cost = abs(xi-xj) + abs(yi-yj)
                
                #Undirected Edges
                adjList[i].append([j, cost])
                adjList[j].append([i, cost])
        print(adjList)
        #Prims algorithm - make minimum spanning tree where each point is connected with minimum cost 
        #Using minheap
        minHeap = []
        
        #Populate minheap with neighbours, sorted from lowest cost property
        for nei, weight in adjList[0]:
            heapq.heappush(minHeap, [weight, 0, nei])
        
        print(minHeap)
        mst = []
        mstCost = 0
        visit = set()
        visit.add(0)
        
        #When all points are visited, there is one path between each pair of points
        #Where the minimum cost is the path taken between each point using the minimum heap
        
        while len(visit) != len(points):
            pointCost, src, dst = heapq.heappop(minHeap)
            
            #If we already visited dst, ignore, as we already took its mincost
            if dst in visit:
                continue
            
            visit.add(dst)
            mst.append([src, dst])
            mstCost += pointCost
            for n2, w2 in adjList[dst]:
                if n2 not in visit:
                    heapq.heappush(minHeap, [w2, dst, n2])
    

        return mstCost
        

        

        