class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        indegrees = [0]*(n+1)
        adj = {i:[] for i in range(n+1)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indegrees[u] +=1
            indegrees[v] +=1
        q = deque()

        for i in range(len(indegrees)):
            if indegrees[i] == 1:
                q.append(i)
        index = 0
        while q:
            pre = q.popleft()
            for post in adj[pre]:
                indegrees[post]-=1
                if indegrees[post] == 1:
                    q.append(post)
        edges = edges[::-1]
        for u, v in edges:
            if indegrees[u] == 2 and indegrees[v] == 2:
                return [u,v]

        