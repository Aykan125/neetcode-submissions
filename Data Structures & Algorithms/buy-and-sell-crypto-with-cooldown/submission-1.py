class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy on b sell today: dfs(b, s):
        #profit = b-s -> dfs(b+2, s+2)
        #buy on b do nothing -> dfs(b, s+1)
        #
        dp = {}
        def dfs(i, canBuy):
            if i >= len(prices):
                return 0
            if (i, canBuy) in dp:
                return dp[(i, canBuy)]

            if canBuy:
                bought = dfs(i+1, not canBuy) - prices[i]
                skip = dfs(i+1, canBuy)
                profit = max(bought, skip)
            else:
                sold = dfs(i+2, not canBuy) + prices[i]
                skip = dfs(i+1, canBuy)
                profit = max(sold, skip)
            dp[(i, canBuy)] = profit
            return dp[(i, canBuy)]
        return dfs(0, True)
        