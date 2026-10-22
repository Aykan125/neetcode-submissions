class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #1->2->3
        #2->1->3
        #2->3->1
        output = []
        perms = []
        pick = [False]*len(nums)
        def dfs():
            if len(nums) == len(perms):
                output.append(perms.copy())
                return
            for i in range(len(nums)):
                if not pick[i]:
                    perms.append(nums[i])
                    pick[i] = True
                    dfs()
                    perms.pop()
                    pick[i] = False
        dfs()
        return output

        