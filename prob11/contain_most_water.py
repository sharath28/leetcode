class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        # for i in range(len(height)):
        #     for j in range(i+1,len(height)):
        #         if height[i]<height[j]:
        #             temp_area = height[i]*(j-i)
        #         else:
        #             temp_area = height[j]*(j-i)
        #         if max_area <temp_area:
        #             max_area = temp_area
        # return max_area
        l = 0
        r = len(height)-1
        while l<r:
                if height[l]<height[r]:
                    temp_area = height[l]*(r-l)
                else:
                    temp_area = height[r]*(r-l)
                if max_area <temp_area:
                    max_area = temp_area
                if height[l]<height[r]:
                    l +=1
                else:
                    r -= 1
        return max_area
