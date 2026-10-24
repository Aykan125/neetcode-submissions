class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False
        visited = set()

        adj = {i:[] for i in range(n)}

        for out, indegree in edges:
            adj[out].append(indegree)
            adj[indegree].append(out)
        def dfs(node, previous):
            if node in visited:
                return False
            visited.add(node)
            for k in adj[node]:
                if k == previous:
                    continue
                if not dfs(k, node):
                    return False
            # visited.remove(node)
            return True
        return dfs(0, -1) and len(visited) == n



            
        