class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        next_max = {}
        for i in range(len(nums2)):
            if i==len(nums2)-1:
                next_max[nums2[i]]=-1
                break
            j = i
            temp = 0
            while j<len(nums2):
                if nums2[j]>nums2[i]:
                    next_max[nums2[i]]=nums2[j]
                    temp = 1
                    break
                else:
                    j += 1
            if temp == 0:
                next_max[nums2[i]]=-1
        final_list = []
        for num in nums1:
            final_list.append(next_max[num])
            # if next_max>num:
            #     final_list.append(next_max)
            # else:
            #     final_list.append(-1)
        return final_list
