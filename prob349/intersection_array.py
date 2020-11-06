class Solution(object):
    def set_intersection(self,set1,set2):
            return [x for x in set1 if x in set2]

    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        # nums1_dict = {}
        # nums2_dict = {}
        # for num in nums1:
        #     nums1_dict[num]=1
        # for num in nums2:
        #     nums2_dict[num]=1
        # final_list = []
        # for num in nums1_dict:
        #     if num in nums2_dict:
        #         final_list.append(num)
        # return final_list
        set1 = set(nums1)
        set2 = set(nums2)

        # m*n
        if len(set1)<len(set2):
            return self.set_intersection(set1,set2)
        else:
            return self.set_intersection(set2,set1)

        # Inbuilt
        # return list(set2 & set1)
