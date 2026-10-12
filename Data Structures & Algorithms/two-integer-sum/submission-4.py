class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]+nums[j] == target:
        #            return [i,j]
        # set for nums
        #7-3
        num_dict = {}
        for j in range(len(nums)):
            num_dict[nums[j]] = j
        for i in range(len(nums)):

            if (target - nums[i]) in num_dict and (i != num_dict[target -nums[i]]) :
                return [i, num_dict[target -nums[i]]]
        