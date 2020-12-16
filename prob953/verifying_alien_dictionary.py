class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        def check_word(first_word,second_word,word_dict):
            i = 0
            j = 0
            while i < len(first_word) and j < len(second_word):
                if word_dict[first_word[i]] == word_dict[second_word[j]]:
                    i += 1
                    j += 1
                    continue
                elif word_dict[first_word[i]] < word_dict[second_word[j]]:
                    return True
                elif word_dict[first_word[i]] > word_dict[second_word[j]]:
                    return False
            if len(first_word)<=len(second_word):
                return True
            else:
                return False

        word_dict = {}
        for i,v in enumerate(order):
            word_dict[v] = i
        for i in range(len(words)-1):
            first_word = words[i]
            second_word = words[i+1]
            return_val = check_word(first_word,second_word,word_dict)
            if return_val == False:
                return False
            else:
                continue
        return True
