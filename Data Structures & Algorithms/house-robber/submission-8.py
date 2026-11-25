class Solution:
    def rob(self, nums: List[int]) -> int:

        # memo = {}

        # def dfs(i):
        #     if i in memo:
        #         return memo[i]
        #     if i >= len(nums):
        #         return 0
        #     memo[i] = max(nums[i]+dfs(i+2), dfs(i+1))
        #     return memo[i]
        # return dfs(0)


        dp = {len(nums)-1:nums[-1], len(nums):0}
        for i in range(len(nums) - 2, -1, -1):
            dp[i] = max(nums[i] + dp[i+2], dp[i+1])
        return dp[0]
        