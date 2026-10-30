class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for i in strs:
            res.append(str(len(i)))
            res.append("#")
            res.append(i)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        i = 0
        while i<len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            i = j+1
            res.append(s[i:i+length])
            i = i+length
        return res


