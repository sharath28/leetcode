class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        final_list = []
        max_count = max(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies>=max_count:
                final_list.append(True)
            else:
                final_list.append(False)
        return final_list
