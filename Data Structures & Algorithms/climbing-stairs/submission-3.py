class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {n+1:0, n:1}
        # def dfs(i):
        #     if i in memo:
        #         return memo[i]
        #     if i > n:
        #         return 0
        #     if i == n:
        #         return 1
            
        #     calc = dfs(i+1) + dfs(i+2)
        #     memo[i] = calc

        #     return memo[i]
        # return dfs(0)
        

        for i in range(n - 1, -1, -1):

            dp[i] = dp[i+1] + dp[i+2]
        return dp[0]

        