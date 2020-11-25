class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        char_dict = {}
        for char in nums:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
        # final_string = ""
        sorted_list = sorted(char_dict.items(), key =
             lambda kv:(kv[1],-kv[0]))
        final_list = []
        for char_val in sorted_list:
            final_list += [char_val[0]]*char_val[1]
        return final_list
