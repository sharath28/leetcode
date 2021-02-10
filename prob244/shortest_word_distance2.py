class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.words = words
        self.temp_dict = {}
        for i in range(len(words)):
            if words[i] not in self.temp_dict:
                self.temp_dict[words[i]] = [i]
            else:
                self.temp_dict[words[i]].append(i)


    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        maxi = sys.maxint
        list1 = self.temp_dict[word1]
        list2 = self.temp_dict[word2]
        for i in range(len(list1)):
            for j in range(len(list2)):
                if abs(list1[i]-list2[j])<maxi:
                    maxi = abs(list1[i]-list2[j])
        return maxi


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
