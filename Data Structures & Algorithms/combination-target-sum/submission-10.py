from collections import Counter
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #[2]->[2]->[2]->[2]
        output = []
        subset = []
        def dfs(i):
            if sum(subset) == target:
                output.append(subset.copy())
                return
            elif sum(subset) > target or i>= len(nums):
                return
            subset.append(nums[i])
            dfs(i)
            subset.pop()
            dfs(i+1)
        dfs(0)
        # print(output)
        return output
        