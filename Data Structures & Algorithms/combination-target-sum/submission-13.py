class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        subset = []
        def dfs(i, cSum):

            if i>=len(nums) or cSum>target:
                return
            if cSum == target:
                output.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i, cSum+nums[i])
            subset.pop()
            dfs(i+1, cSum)
            return
        dfs(0, 0)
        return output
        