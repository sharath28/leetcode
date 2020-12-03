class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prod = 1
        count = 0
        for num in nums:
            if num == 0:
                count += 1
                continue
            prod *= num

        return_list = []
        if count >= 2:
            return [0]*len(nums)
        if count == 1:
            for num in nums:
                if num == 0:
                    return_list.append(prod)
                else:
                    return_list.append(0)
            return return_list
        for num in nums:
            if num == 0:
                return_list.append(prod)
                continue
            return_list.append(prod//num)
        return return_list
