class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp_list = s.split(' ')
        final_list = []
        for word in temp_list:
            final_list.append(word[::-1])

        return ' '.join(final_list)
