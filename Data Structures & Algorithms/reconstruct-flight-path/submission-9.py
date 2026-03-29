#We're given a list of tickets of 2 tuples src, dst
#Where src and dst consist of uppercase english letters
#We need to reconstruct the flight iternary in lexical order, where each flight always starts at "JFK"

#We can use DFS to find a valid path starting from JFK, while making sure not to reuse the same tickets
#We can also sort the tickets Lexically to find the lexically sorted path in dfs
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
      
        adjList = defaultdict(list)
        
        tickets.sort()
      
        #populate adjlist w/ lexically sorted edges
        for src, dst in tickets:
            adjList[src].append(dst)
        
        ticketSet = set()
        path = ["JFK"]
        print(adjList)
        def dfs(node, adjList):
            #If we used all tickets return True, as we found the 
            if len(ticketSet) == len(tickets):
                    return True
            
            #If we arrived at the last dest, return
            if node not in adjList:
                return False
            

            for i, nei in enumerate(adjList[node]):
                
                if (node, i) not in ticketSet:
                    ticketSet.add((node,i))
                    path.append(nei)
                    
                    if dfs(nei, adjList):
                        return True
                    
                    path.pop()
                    ticketSet.remove((node,i))
                    
            return False
        
        if dfs("JFK", adjList):
            return path


        

        
        
        