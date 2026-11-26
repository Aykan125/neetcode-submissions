class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def dfs(i):
            if i in memo:
                return memo[i]
            if i>=len(temp):
                return 0
            memo[i] = max(temp[i] + dfs(i+2), dfs(i+1))
            return memo[i]
        temp = nums[1:]
        memo = {}
        val1 = dfs(0)
        memo = {}
        temp = nums[:-1]
        val2 = dfs(0)
        return max(val1, val2)
        
        