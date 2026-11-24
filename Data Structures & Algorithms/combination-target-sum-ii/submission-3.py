class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        subset = []
        candidates.sort()
        def dfs(i, cSum):
            if cSum == target:
                output.append(subset.copy())
                return
            if i>=len(candidates) or cSum > target:
                return

            subset.append(candidates[i])
            dfs(i+1, cSum+candidates[i])
            subset.pop()
            while i<len(candidates)-1 and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1, cSum)
            return
        dfs(0, 0)
        return output

        