class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        #prerequisites -> course
        indegree = [0]*(numCourses)

        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] +=1
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        while q:
            node = q.popleft()

            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei] == 0:
                    q.append(nei)
        for j in range(len(indegree)):
            if indegree[j]>0:
                return False
        return True

        
        