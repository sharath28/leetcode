class Solution(object):
    def check_intersection(self,nums1,nums2):
        return_list = []
        for num in nums1:
            if num in nums2:
                return_list.append(num)
                nums2.remove(num)
        return return_list

    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1)<len(nums2):
            return self.check_intersection(nums1,nums2)
        else:
            return self.check_intersection(nums2,nums1)
