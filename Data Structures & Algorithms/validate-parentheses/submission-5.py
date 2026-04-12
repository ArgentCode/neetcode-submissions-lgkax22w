class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        stack = []
        for i in range(n):
            val = s[i]
            if val in ["[", "{", "("]:
                stack.append(val)
            elif val == "]":
                if len(stack) == 0: return False
                comp = stack.pop()
                if comp != "[":
                    return False
            elif val ==")":
                if len(stack) == 0: return False
                comp = stack.pop()
                if comp != "(":
                    return False
            elif val =="}":
                if len(stack) == 0: return False
                comp = stack.pop()
                if comp != "{":
                    return False
        if len(stack) > 0:
            return False
        return True


        