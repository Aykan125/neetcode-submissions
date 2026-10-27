class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 != 0 :
            return False

        memo = {}

        target = sum(nums)//2

        def dfs(i, t):
            if (i, t) in memo:
                return memo[(i,t)]
            if t == 0:
                return True
            if i>=len(nums) or t<0:
                return False

            memo[(i, t)] =  dfs(i+1, t) or dfs(i+1, t - nums[i])
            return memo[(i,t)]
        return dfs(0, target)
            
        