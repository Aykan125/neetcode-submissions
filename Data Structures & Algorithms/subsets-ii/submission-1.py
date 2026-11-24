class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = []
        subset = []
        nums.sort()
        def dfs(i):
            output.append(subset.copy())
                
            for k in range(i, len(nums)):
                if k>i and nums[k] == nums[k-1]:
                    continue
            
                subset.append(nums[k])
                dfs(k+1)
                subset.pop()
            return
        dfs(0)
        return output
                
        