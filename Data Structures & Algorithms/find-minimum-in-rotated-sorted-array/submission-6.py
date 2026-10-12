class Solution:
    def findMin(self, nums: List[int]) -> int:
        # l,r = 0, len(nums) - 1
        # res = nums[0]

        # while l<=r:
        #     if nums[l] < nums[r]:
        #         res = min(res, nums[l])
        #         break
        #     m = l+((r-l)//2)
        #     res = min(nums[m],res)
        #     if nums[m]>nums[l]:
        #         l=m+1
        #     else:
        #         r = m - 1
        # return res
        l, r = 0, len(nums) - 1

        while l < r:
            m = l + (r - l) // 2

            if nums[m] > nums[r]:
                # Minimum is strictly to the right of m
                l = m + 1
            else:
                # nums[m] could be the minimum
                r = m

        return nums[l]