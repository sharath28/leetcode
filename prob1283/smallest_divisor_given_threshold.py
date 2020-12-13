class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        compute_sum = lambda x: sum([ceil(n/float(x)) for n in nums])
        # d = 1
        # while compute_sum(d)>threshold:
        #     d += 1
        # return d
        left, right = 1,2
        while compute_sum(right)>threshold:
            left = right
            right <<= 1

        while left <= right:
            pivot = (right + left) >> 1
            num = compute_sum(pivot)

            if num> threshold:
                left = pivot + 1
            else:
                right = pivot - 1
        return left
