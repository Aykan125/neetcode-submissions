class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        tickets = tickets[::-1]
        adj = defaultdict(list)
        for src, dst in tickets:
            adj[src].append(dst)

        res = []

        def dfs(flight):
            while adj[flight]:
                dst = adj[flight].pop()
                dfs(dst)
            res.append(flight)
        dfs("JFK")
        return res[::-1]
            

        