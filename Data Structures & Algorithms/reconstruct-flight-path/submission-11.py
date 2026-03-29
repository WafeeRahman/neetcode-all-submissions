#We're given a list of tickets of 2 tuples src, dst
#Where src and dst consist of uppercase english letters
#We need to reconstruct the flight iternary in lexical order, where each flight always starts at "JFK"

#We can use DFS to find a valid path starting from JFK, while making sure not to reuse the same tickets
#We can also sort the tickets Lexically to find the lexically sorted path in dfs
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
      
        adjList = defaultdict(list)
        
        tickets.sort()
      
        #Populate adjlist w/ lexically sorted edges
        for src, dst in tickets:
            adjList[src].append(dst)
        
        #Keep Track of Used Tickets
        ticketSet = set()
        #Start at JFK
        path = ["JFK"]
        
        print(adjList)
        
        #DFS and Backtrack to find A Valid Path
        def dfs(node, adjList):
            #If we used all tickets return True, as we found the 
            if len(ticketSet) == len(tickets):
                    return True
            
            #If we arrived at a dead end where we havent used all tickets, return false
            if node not in adjList:
                return False
            
            #Iterate through every neighbour and their index relative to adjlist node
            #As the same DST can appear twice in this ADJlist
            for i, nei in enumerate(adjList[node]):
                
                #If we didnt already use this ticket
                if (node, i) not in ticketSet:
                    #Use it and run DFS on the neighbour to see if we get a valid path
                    #That is lexically sorted
                    ticketSet.add((node,i))
                    path.append(nei)
                    
                    #If we do return True
                    if dfs(nei, adjList):
                        return True

                    #OTWS backtrack and find a path where all tickets are used
                    path.pop()
                    ticketSet.remove((node,i))
                    
            return False #Return false to previous call, as we didnt find a valid path at current node
        
        if dfs("JFK", adjList):
            return path


        

        
        
        