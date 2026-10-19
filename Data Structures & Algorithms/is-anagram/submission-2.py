class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        sArr = [0]*26
        for i in range(len(s)):
            sArr[ord(s[i]) - ord("a")] +=1
            sArr[ord(t[i]) - ord("a")] -=1
        for val in sArr:
            if val != 0:
                return False
        return True
        