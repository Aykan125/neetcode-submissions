class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        a = len(nums)-1
        return max(self.rob1(nums[:a]), self.rob1(nums[1:]))
    def rob1(self, arr):
        arr.reverse()
        rob3, rob4 = 0, 0
        for i in arr:
            newRob = max(i+rob4, rob3)
            rob4 = rob3
            rob3 = newRob
        return rob3

        
        