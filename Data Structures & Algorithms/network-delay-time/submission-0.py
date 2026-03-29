#We are given a network of n directed nodes, labeled from 1 .. n. We are given times, a group of directed
#Edges with weight, where ui is the soruce node, vi is the target node, and ti is the time(weight they share)
#We are given a node k, representing the node that we will send a signal from

#We need to return the time it takes for all n nodes to receive the signal from node k

#In english: we're given a graph with n nodes and a group of directed edges w/ weight, we need to find the total time
#Where we can reach all nodes from node k
#To find the minimum time, we need to use the shortest path to each node from k, therefore, lets use djikstras algorithm
#To find the shortest path from k to all the other nodes

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list) #Node -> list of neighbours
        #since a network is a connected graph, we can use a default dict, since every node is connected
        for u, v, t in times:
            adj[u].append((v, t)) #Connect edges

        minHeap = [(0, k)]
        shortest = {}

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            
            if n1 in shortest:
                continue
            
            shortest[n1] = w1
            
            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, ((w1+w2), n2))
                continue
        
        for i in range(1, n+1):
            if i not in shortest:
                return -1
        return max(shortest.values())





        