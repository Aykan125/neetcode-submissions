class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        #take a letter from a
        #take a letter from b
        #if we reach the end of a, we check if the remainder of b can resolve the remainder of c -> if not we reject, if it can we accept

        #if niether a, or b have the letter currently pointing at c, then return
        dp = {}

        def dfs(i, j, k):
            if (i,j) in dp:
                return dp[(i,j)]
            if k == len(s3):
                return i == len(s1) and j == len(s2)

            
            res = False
            if i < len(s1) and s1[i] == s3[k]:
                res = dfs(i+1, j, k+1)
            if not res and j<len(s2) and s2[j] == s3[k]:
                res = dfs(i, j+1, k+1)
            dp[(i,j)] = res
            return dp[(i,j)]
        return dfs(0,0,0)
            
                

            
            
        