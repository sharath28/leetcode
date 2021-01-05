class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        b = 0
        c = 0
        secret_dict = {}
        guess_dict = {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                b += 1
            else:
                if guess[i] not in guess_dict:
                    guess_dict[guess[i]] = 1
                else:
                    guess_dict[guess[i]] += 1
                if secret[i] not in secret_dict:
                    secret_dict[secret[i]] = 1
                else:
                    secret_dict[secret[i]] += 1

        for guess in guess_dict:
            if guess in secret_dict:
                if secret_dict[guess] > guess_dict[guess]:
                    c += guess_dict[guess]
                else:
                    c += secret_dict[guess]


        return str(b)+'A'+str(c)+'B'
