class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        i = j = 0
        n = len(prices)
        while i < n and j < n:
            if prices[i] <= prices[j]:
                mp = max(mp, prices[j] - prices[i])
            else:
                i = j
            j += 1 

        return mp