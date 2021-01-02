from copy import copy
class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        return_list = []
        char_dict = {}
        count = 0
        for ch in chars:
            if ch not in char_dict:
                char_dict[ch] = 1
            else:
                char_dict[ch] += 1

        for word in words:
            flag = 0
            temp = copy(char_dict)
            for ch in word:
                if ch not in temp:
                    flag = 1
                    break
                else:
                    if temp[ch] == 0:
                        flag = 1
                    else:
                        temp[ch] -= 1
            if flag == 0:
                count += len(word)
        return count
