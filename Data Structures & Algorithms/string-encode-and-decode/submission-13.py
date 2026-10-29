class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res+=i
            res+="§"
        return res

    def decode(self, s: str) -> List[str]:
        ptr = 0
        res = []
        temp = ""
        while ptr < len(s):
            if s[ptr] == "§":
                res.append(temp)
                temp = ""
            else:
                temp+=s[ptr]
            ptr+=1
        return res
