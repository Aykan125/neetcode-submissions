class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sArr = [0]*26
        tArr = [0]*26
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            sArr[ord(s[i]) - ord("a")] +=1
            tArr[ord(t[i]) - ord("a")] +=1
        return sArr == tArr
        