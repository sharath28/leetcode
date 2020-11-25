class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        char_dict = {}
        for char in s:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
        final_string = ""
        sorted_list = sorted(char_dict.items(), key =
             lambda kv:(kv[1], kv[0]), reverse=True)
        for char_val in sorted_list:
            final_string += char_val[0]*char_val[1]
        return final_string
