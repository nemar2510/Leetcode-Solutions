class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        low=prices[0]
        max_profit=0
        for i in range(len(prices)):
            if prices[i]<low:
                low=prices[i]
            profit=prices[i]-low
            if profit>max_profit:
                max_profit=profit
        return max_profit
            