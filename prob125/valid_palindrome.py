class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        punctuations = '''`!()-[]{};:'"\,<>./?@#$%^&*_~'''
        no_punct = ""
        for char in s:
            if char not in punctuations:
                no_punct = no_punct + char

        # display the unpunctuated string
        no_punct = no_punct.replace(" ", "").lower()
        if no_punct == no_punct[::-1]:
            return True
        else:
            return False
        
