#Given a 2D nxn matrix where grid[i][j] represents the elevation at position i,j
#Rain falls at time zero, which makes the elevation ries for each cell, where at time t the water across the entire grid is t
#We can either traverse horizontally or vertically in the grid if the adjacent cells elevation are <= to the water at time t
#We need to find the minimum amount of time until its possible to reach the bottom right square n-1 n-1
#We know that the max elevation we need is the MAX elevation we encounter in the shortest path to n-1 n-1
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        #Populate Adjacency list
        ROWS = len(grid)
        COLS = len(grid[0])
        adj = defaultdict(list)
        for i in range(ROWS):
            for j in range(COLS):
                #We can only travel to adjacent neighbours (edges)
                if j+1 < COLS:
                    adj[(i,j)].append([(i,j+1), grid[i][j+1]])
                    adj[(i,j+1)].append([(i,j), grid[i][j]])
                
                if i+1 < ROWS:
                    adj[(i, j)].append([(i+1, j), grid[i+1][j]])
                    adj[(i+1, j)].append([(i, j), grid[i][j]])
        
        

        #Apply Djikstra's Algorithm to Compute The Shortest Path from 0, 0 to n-1 n-1

        minHeap = [[grid[0][0], (0,0)]]   
        shortest = {}
        maxCost = float('-inf')
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in shortest:
                continue
            shortest[n1] = w1
            for nei in adj[n1]:
                if nei[0] not in shortest:
                    heapq.heappush(minHeap, [max(nei[1], w1), nei[0]]) #Maintgain the max cost for the current path

        return shortest[(ROWS-1, COLS-1)]


     
                            