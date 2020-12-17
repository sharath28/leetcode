class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        best = 1
        for i in range(2, int(sqrt(area)) + 1):
            if area % i == 0:
                best = i

        return sorted([area // best, best], reverse=True)
