import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        res = r

        while l<=r:
            m = l+((r-l)//2)
            print(l,m,r)
            hours_spent = 0
            for j in piles:
                hours_spent += math.ceil(j/m)
            if hours_spent <= h:
                res = m
                r = m-1
            else:
                l = m+1
        return res

        