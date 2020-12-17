class Solution(object):
    def checkWord(self,word,letter_dict):
        for char in word:
            temp = char.lower()
            if temp not in letter_dict:
                return False
        return True

    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        first_row = {"q":1,"w":1,"e":1,"r":1,"t":1,"y":1,"u":1,"i":1,"o":1,"p":1}
        second_row = {"a":1,"s":1,"d":1,"f":1,"g":1,"h":1,"j":1,"k":1,"l":1}
        third_row = {"z":1,"x":1,"c":1,"v":1,"b":1,"n":1,"m":1}
        final_list = []
        for word in words:
            if word[0].lower() in first_row:
                if self.checkWord(word,first_row):
                    final_list.append(word)
            elif word[0].lower() in second_row:
                if self.checkWord(word,second_row):
                    final_list.append(word)
            elif word[0].lower() in third_row:
                if self.checkWord(word,third_row):
                    final_list.append(word)
        return final_list
