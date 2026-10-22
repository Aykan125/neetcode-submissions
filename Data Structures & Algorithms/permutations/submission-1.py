class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #1->2->3
        #2->1->3
        #2->3->1
        output = []
        pick = set()
        perms = []

        def dfs():
            if len(perms) == len(nums):
                output.append(perms.copy())
                return
            for i in range(len(nums)):
                if nums[i] not in pick:
                    perms.append(nums[i])
                    pick.add(nums[i])
                    dfs()
                    pick.remove(nums[i])
                    perms.pop()
        dfs()
        return output
                    


        