class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        buy = 0
        i = 1
        while i < n:
            if prices[i] > prices[buy]:
                profit += prices[i] - prices[buy]
                buy = i  
            elif prices[i] < prices[buy]: 
                buy = i
            i += 1
        return profit