class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        cur = self.trie
        for i in word:
			if i not in cur:
				cur[i] = {}
			cur = cur[i]
        print(self.trie)
        cur["#"] = "#"


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.trie
        for i in word:
			if i not in cur:
				return False
			cur = cur[i]
        if "#" in cur:
			return True

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.trie
        for i in prefix:
			if i not in cur:
				return False
			cur = cur[i]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
