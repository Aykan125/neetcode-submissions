class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        for i in range(len(nums)):
            l, r= i+1, len(nums) - 1
            if i>0 and nums[i]==nums[i-1]:
                continue
            while l<r:
                if nums[i] + nums[l] + nums[r] == 0:
                    output.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l - 1] and l < r:
                        l+=1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l+=1
                    while nums[l] == nums[l - 1] and l < r:
                        l+=1
                else:
                    r-=1
        return output



        