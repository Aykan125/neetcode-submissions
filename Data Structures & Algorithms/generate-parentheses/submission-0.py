class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        brackets = []
        def dfs(openN, closedN):
            if openN == closedN == n:
                output.append("".join(brackets))
                return
            if openN<n:
                brackets.append("(")
                dfs(openN+1, closedN)
                brackets.pop()
            if closedN < openN:
                brackets.append(")")
                dfs(openN, closedN+1)
                brackets.pop()
        dfs(0,0)
        return output