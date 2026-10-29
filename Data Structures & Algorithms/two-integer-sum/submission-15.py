class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twoSUMMED = {}

        for j, i in enumerate(nums):
            if target - i in twoSUMMED:
                return [twoSUMMED[target-i], j]
            else:
                twoSUMMED[i] = j
        print(twoSUMMED)
        

        