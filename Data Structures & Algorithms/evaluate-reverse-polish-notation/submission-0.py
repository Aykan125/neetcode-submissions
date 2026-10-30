class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in ["+", "-","/","*"]:
                num2 = stack.pop()
                num1 = stack.pop()
                if i == "+":
                    num3 = num1 + num2
                elif i == "-":
                    num3 = num1 - num2
                elif i == "*":
                    num3 = num1*num2
                else:
                    num3 = int(num1/num2)

                stack.append(num3)
            else:
                stack.append(int(i))
        return stack[-1]
        