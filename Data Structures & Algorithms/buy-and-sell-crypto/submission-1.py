class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # if r<l - shift l ++ and r++ and buy -> l = buy
        # if r>l - shift r++ cal sell profit (diff) -> r = sell
        # until r ends iterate all elemenets - take max profit diff


        l, r = 0, 1

        maxProfit = 0

        while r < len(prices):

            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l=r
            r+=1
            
        return maxProfit
        



        