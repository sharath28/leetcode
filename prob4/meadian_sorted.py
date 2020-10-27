class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        temp_list = nums1+nums2
        temp_list.sort()
        if len(temp_list)%2==0:
            return (temp_list[len(temp_list)/2]+temp_list[len(temp_list)/2-1])/2.0
        else:
            return temp_list[len(temp_list)/2]
