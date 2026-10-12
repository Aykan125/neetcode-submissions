class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        if not strs:
            return ""
        for i in strs:
            res = res+ i + "."
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        start = 0
        end = 0
        if not s:
            return []

        for i in range(len(s)):
            b = s[start:end]
            if s[i]==".":
                start = i+1
                
                res.append(b)
            
            end+=1
        return res

