class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        output = []
        visited = set()
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        visit = set()

        def dfs(node):
            if node in visit:
                return False
            if not preMap[node]:
                if node not in visited:
                    visited.add(node)
                    output.append(node)
                return True
            visit.add(node)
            for crs in preMap[node]:
                if not dfs(crs):
                    return False
            preMap[node] = []
            visit.remove(node)
            if node not in visited:
                visited.add(node)
                output.append(node)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        # output = output[::-1]
        return output

        