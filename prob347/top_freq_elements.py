class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        words = nums
        word_dict = {}
        for word in words:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
        sort_orders = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
        return_list = []
        for i in range(k):
            return_list.append(sort_orders[i][0])
        return return_list
