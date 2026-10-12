class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums) - 1
        while l<r:
            m = l+((r-l)//2)
            print(l,m,r)
            print(nums[l],nums[m],nums[r])
            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m
        return nums[l]

