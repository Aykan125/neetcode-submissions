class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub, curSum = nums[0], 0

        for i in nums:
            if curSum< 0:
                curSum = 0
            curSum+=i
            maxSub = max(maxSub, curSum)
        return maxSub

        