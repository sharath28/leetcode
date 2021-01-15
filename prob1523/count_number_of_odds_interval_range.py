class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        # return_list = []
        # count = 0
        # for i in range(low,high+1):
        #     if i%2 == 1:
        #         count += 1
        # return count
        if low %2 == 0 and high % 2 == 0:
            return (high-low)//2
        else:
            return (high-low)//2  + 1
