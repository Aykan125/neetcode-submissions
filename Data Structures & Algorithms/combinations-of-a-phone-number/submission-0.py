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
            for k in range(i, len(digits)):
                if k>i:
                    continue
                for h in range(len(dMap[digits[k]])):
                    tString.append(dMap[digits[k]][h])
                    dfs(i+1)
                    tString.pop()
        dfs(0)
        if not output[0]:
            return []
        return output

        