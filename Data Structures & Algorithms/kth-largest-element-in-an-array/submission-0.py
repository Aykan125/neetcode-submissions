class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = nums[i]*-1
        heapq.heapify(nums)
        k-=1
        while k>0:
            heapq.heappop(nums)
            k-=1
        return -1*heapq.heappop(nums)

        