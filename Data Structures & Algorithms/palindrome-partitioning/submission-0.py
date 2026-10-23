class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output = []
        temp = []
        def dfs(i):
            if i>=len(s):
                output.append(temp[:])
                return
            for k in range(i, len(s)):
                if self.isPalindrome(s[i:k+1]):
                    temp.append(s[i:k+1])
                    dfs(k+1)
                    temp.pop()
        dfs(0)
        return output


    def isPalindrome(self, string):
        #odd
        l, r =0,0
        mid = len(string)//2
        if len(string)%2!=0:
            l,r = mid, mid
            while l>-1 and r<len(string) and string[l] == string[r]:
                l-=1
                r+=1
        else:
            l,r = mid - 1, mid
            while l>-1 and r< len(string) and string[l] == string[r]:
                l-=1
                r+=1
        print(l, r)
        if l<0:
            return True
        else:
            return False
        