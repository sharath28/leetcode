class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # if len(prices)<2:
        #     return 0
        # if len(prices)==2:
        #     curr = prices[0]
        #     next_max = max(prices[1:])
        #     if next_max>=curr:
        #         prices[0]=next_max-curr
        #     else:
        #         prices[0]=0
        #     return prices[0]
        # for i in range(len(prices)-1):
        #     curr = prices[i]
        #     next_max = max(prices[i+1:])
        #     if next_max>=curr:
        #         prices[i]=next_max-curr
        #     else:
        #         prices[i]=0
        # return max(prices[:len(prices)-1])
        minPrice = 999999999999
        maxProfit = 0
        for i in range(len(prices)):
            if prices[i]<minPrice:
                minPrice = prices[i]
            elif prices[i]-minPrice > maxProfit:
                maxProfit = prices[i]-minPrice
        return maxProfit
