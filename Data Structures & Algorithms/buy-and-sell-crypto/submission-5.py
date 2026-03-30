class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        maxPrice = 0

        for sell in prices:
            maxPrice = max(maxPrice, sell - minBuy)
            minBuy = min(minBuy, sell)

        return maxPrice
        