class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # if cost[0]<cost[1]:
        #     i = 0
        # else:
        #     i = 1
        # minCost = 0
        # while i < len(cost)-1:
        #     minCost += cost[i]
        #     if cost[i+1]<cost[i+2]:
        #         i += 1
        #     else:
        #         i += 2
        # return minCost

        f1 = f2 = 0
        for x in reversed(cost):
            f1,f2 = x+min(f1,f2),f1
        return min(f1,f2)
