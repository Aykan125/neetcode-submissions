from collections import Counter
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        def dfs(i, s, arr):
            if s == target:
                output.append(arr.copy())
                return
            if s>target or i>=len(nums):
                return
            arr.append(nums[i])
            dfs(i, s+nums[i], arr)
            arr.pop()
            try:
                dfs(i+1, s, arr)
            except Exception as e:
                print(e)
                return

        dfs(0, 0, [])
        return output
        