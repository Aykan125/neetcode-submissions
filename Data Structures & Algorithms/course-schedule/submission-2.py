class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        visited = set()
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(crs):
            if crs in visited:
                return False
            if not preMap[crs]:
                return True
            visited.add(crs)
            for i in range(len(preMap[crs])):
                if not dfs(preMap[crs][i]):
                    return False
            visited.remove(crs)
            preMap[crs] = []
            return True
        for j in range(numCourses):
            for crs in range(len(preMap[j])):
                if not dfs(preMap[j][crs]):
                    return False
        return True
            
                
        