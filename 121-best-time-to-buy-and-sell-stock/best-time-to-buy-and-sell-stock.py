from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, R = 0, 1
        currProfit = 0
        maxProfit = float('-inf')
        while R < len(prices):
            if prices[R]<prices[L]:
                L = R
            else:
                currProfit = prices[R] - prices[L]
                maxProfit = max(currProfit, maxProfit)
            R+=1
        if maxProfit == float('-inf'):
            return 0
        return maxProfit