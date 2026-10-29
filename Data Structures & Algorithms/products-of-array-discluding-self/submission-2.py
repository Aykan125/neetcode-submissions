class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        pre = [1]*len(nums)
        for i in range(len(nums)):
            pre[i] = prefix
            prefix*=nums[i]
        postfix = 1
        for j in range(len(nums)-1, -1, -1):
            pre[j]*=postfix
            postfix*= nums[j]

        return pre