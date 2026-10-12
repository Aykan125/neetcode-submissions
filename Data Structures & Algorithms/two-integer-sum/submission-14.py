class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        translated = {}
        for i in range(len(nums)):
            if target - nums[i] in translated:
                return [translated[target - nums[i]], i]
            else:
                translated[nums[i]] = i
        