class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adj = {}
        emailMap = {}
        for accs in accounts:
            for acc in accs[1:]:
                adj[acc] = []
                emailMap[acc] = accs[0]
        for accs in accounts:
            for i in range(1, len(accs)):
                for j in range(1, len(accs)):
                    if accs[i] == accs[j]:
                        continue
                    adj[accs[i]].append(accs[j])
        print(adj)

        visit = set()
        def dfs(email, path):
            if email in visit:
                return 
            visit.add(email)
            path.add(email)
            for nei in adj[email]:
                
                if nei in visit:
                    continue
                dfs(nei,path)
            
            return
        res = []
        for email in emailMap:
            path = set()
            dfs(email, path)
            if path:
                res.append([emailMap[email]]+sorted(list(path)))
       
        return res

        