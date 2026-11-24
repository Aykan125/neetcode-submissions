class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        numToLett = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        output = []
        subset = []

        def dfs(i):
            if i>=len(digits):
                output.append("".join(subset))
                return
            digit = digits[i]
            for k in range(len(numToLett[digit])):
                subset.append(numToLett[digit][k])
                dfs(i+1)
                subset.pop()
            return
        dfs(0)
        return output
        