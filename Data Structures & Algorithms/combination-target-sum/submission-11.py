class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #[2]->[2]->[2]->[2]
        output = []
        subset = []
        def dfs(i, total):
            if total == target:
                output.append(subset.copy())
                return
            elif total > target or i>= len(nums):
                return
            subset.append(nums[i])
            dfs(i, total + nums[i])
            subset.pop()
            dfs(i+1, total)
        dfs(0,0)
        # print(output)
        return output
        