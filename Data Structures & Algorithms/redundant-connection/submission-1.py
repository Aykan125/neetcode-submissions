class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = [0]*(len(edges)+1)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            indegree[a] +=1
            indegree[b] +=1
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 1:
                q.append(i)
        while q:
            node = q.popleft()

            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei] == 1:
                    q.append(nei)
        for i in range(len(edges)-1, -1, -1):
            if indegree[edges[i][0]] == 2 and indegree[edges[i][1]] == 2:
                return [edges[i][0], edges[i][1]]



        