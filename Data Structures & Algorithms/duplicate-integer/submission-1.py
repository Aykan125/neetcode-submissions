class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = {}
        for i in nums:
            a[i] = 1
        for i in nums:
            a[i]+=1
            if a[i] == 3:
                return True
        return False

         