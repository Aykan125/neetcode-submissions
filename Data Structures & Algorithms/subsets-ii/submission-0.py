class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = []
        subset = []
        nums.sort()
        def dfs(idx):
            output.append(subset[:])
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                subset.append(nums[i])
                dfs(i+1)
                subset.pop()
        dfs(0)
        return output

            




        