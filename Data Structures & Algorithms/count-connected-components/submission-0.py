class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()

        adj = {i:[] for i in range(n)}

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node, prev):
            if node in visit:
                return
            visit.add(node)
            for v in adj[node]:
                if v == prev:
                    continue
                dfs(v, node)
            return 
        count =0
        # print(visit)
        for i in range(n):
            if i in visit:
                continue
            dfs(i, -1)
            count+=1
        return count
        