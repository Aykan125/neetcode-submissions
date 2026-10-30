class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ["(", "[", "{"]:
                stack.append(i)
            else:
                if stack:
                    if stack[-1] == "(" and i != ")":
                        return False
                    elif stack[-1] == "[" and i != "]":
                        return False
                    elif stack[-1] == "{" and i != "}":
                        return False
                    else:
                        stack.pop()
                else:
                    return False
        if stack:
            return False
        return True

        