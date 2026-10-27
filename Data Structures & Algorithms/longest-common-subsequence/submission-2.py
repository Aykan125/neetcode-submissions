class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]
        print(dp)
        memo = {}
        n = len(text1)
        m = len(text2)

        for i in range(n-1, -1, -1):
            for j in range(m-1,-1,-1):
                dp[i][j] = 1
                if text1[i] == text2[j]:
                    dp[i][j]+=dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
            
        return dp[i][j]

        def dfs(i, j):
            
            if (i,j) in memo:
                return memo[(i,j)]
            if i>=len(text1) or j>=len(text2):
                return 0

            LCS = 1
            if text1[i] == text2[j]:
                LCS+=dfs(i+1, j+1)
            else:
                LCS = max(dfs(i+1, j), dfs(i, j+1))
            
            memo[(i,j)] = LCS
            return memo[(i,j)]
        return dfs(0,0)
        