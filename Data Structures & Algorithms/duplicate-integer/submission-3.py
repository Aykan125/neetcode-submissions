class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unq = set()
        for i in nums:
            if i in unq:
                return True
            else:
                unq.add(i)
        return False
            
        