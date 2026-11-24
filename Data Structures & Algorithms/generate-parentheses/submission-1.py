class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        output = []

        def dfs(openC, closedC):
            if openC == closedC == n:
                output.append("".join(stack))
                return
            
            if openC < n:
                stack.append("(")
                dfs(openC+1, closedC)
                stack.pop()
            if closedC < openC:
                stack.append(")")
                dfs(openC, closedC+1)
                stack.pop()
            return

        dfs(0,0)
        return output
        