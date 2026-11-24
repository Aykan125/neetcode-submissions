class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        pick = [False]*len(nums)
        subset = []
        output = []
        def dfs(i):
            if i >= len(nums):
                output.append(subset.copy())
                return
            for k in range(0, len(nums)):
                if not pick[k]:
                    subset.append(nums[k])
                    pick[k] = True
                    dfs(i+1)
                    subset.pop()
                    pick[k] = False
        dfs(0)
        return output

        