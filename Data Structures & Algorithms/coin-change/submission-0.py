class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(num):
            if num == 0:
                return 0
            if num in memo:
                return memo[num]
            
            res = float("INF")
            for coin in coins:
                if num - coin >= 0:
                    res = min(res, 1 + dfs(num - coin))
            memo[num] = res
            return res
        minC = dfs(amount)
        return -1 if minC==float("INF") else minC

        