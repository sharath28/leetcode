from random import random
class Codec:
    def __init__(self):
        self.url_dict = {}
        self.count = 0

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        # self.url_dict[self.count]= longUrl
        # return "http://tinyurl.com/" + str(self.count)
        # self.count += 1

        r=int(random()*100000)
        while r in self.url_dict:
            r=int(random()*100000)
        self.url_dict[r]= longUrl
        return "http://tinyurl.com/" + str(r)


    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        val = shortUrl.replace("http://tinyurl.com/","")
        return self.url_dict[int(val)]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
