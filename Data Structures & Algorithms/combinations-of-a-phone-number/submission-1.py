class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        output = []
        tString = []
        dMap = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        def dfs(i):
            if i>=len(digits):
                output.append("".join(tString))
                return
            for h in range(len(dMap[digits[i]])):
                tString.append(dMap[digits[i]][h])
                dfs(i+1)
                tString.pop()
        if digits:

            dfs(0)
        

        return output

        