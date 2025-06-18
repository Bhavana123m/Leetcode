class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buying_price = prices[0]
        max_profit = 0
        for price in prices:
            if buying_price < price:
                max_profit += price - buying_price
            buying_price = price
        return max_profit
            
