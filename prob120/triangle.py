class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 0: return 0
        cum_sum = copy.copy(triangle[-1])
        for i in reversed(range(len(triangle)-1)):
            for j in range(i+1):
                cum_sum[j] = triangle[i][j] + min(cum_sum[j], cum_sum[j+1])
        return cum_sum[0]
