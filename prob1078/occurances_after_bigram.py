class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        word_list = text.split(' ')
        bigram = {}
        i = 0
        return_list = []
        while i < len(word_list)-2:
            if word_list[i] == first and word_list[i+1] == second:
                return_list.append(word_list[i+2])
            i += 1
        return return_list
