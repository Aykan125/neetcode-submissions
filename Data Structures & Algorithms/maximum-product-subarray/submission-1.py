class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        minProd = 1
        maxProd = 1
        for i in nums:
            # if i == 0:
            #     n = 1
            # else:
            #     n=i
            n=i
            tmp = minProd
            minProd = min(n, n*tmp, n*maxProd)
            maxProd = max(n, n*tmp, n*maxProd)
            res = max(res, maxProd)
        return res

        