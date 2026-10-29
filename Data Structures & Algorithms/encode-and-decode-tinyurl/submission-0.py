class Solution:
    def __init__(self):
        self.encodeMap = {}
        self.decodeMap = {}
        self.base = "http://tinyurl.com/"
    def encode(self, longUrl: str) -> str:
        if longUrl not in self.encodeMap:
            shortURL = self.base + str(len(self.encodeMap)+1)
            self.encodeMap[longUrl] = shortURL
            self.decodeMap[shortURL] =longUrl
        return self.encodeMap[longUrl]

    def decode(self, shortUrl: str) -> str:
        return self.decodeMap[shortUrl]
        
