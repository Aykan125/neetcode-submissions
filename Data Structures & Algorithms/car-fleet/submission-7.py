class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p,s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)
        for i in range(len(pairs)):
            pairs[i] = (target - pairs[i][0])/pairs[i][1]
        maxT = float("-INF")
        res = 0
        for i in pairs:
            if i>maxT:
                res+=1
                maxT = i
        return res
        