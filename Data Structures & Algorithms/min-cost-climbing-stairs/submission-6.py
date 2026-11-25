class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # memo = {}

        # def dfs(i):
        #     if i in memo:
        #         return memo[i]
        #     if i>=len(cost):
        #         return 0
            
        #     memo[i] = cost[i] + min(dfs(i+1), dfs(i+2))
        #     return memo[i]
        # return min(dfs(0), dfs(1))
        dp = {len(cost)-1:cost[-1], len(cost):0}
        for i in range(len(cost)-2, -1, -1):
            dp[i] = cost[i] + min(dp[i+1], dp[i+2])
        return min(dp[0], dp[1])
            
        