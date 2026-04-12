class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        stack = []
        for i in range(n):
            val = s[i]
            if val in "([{":
                stack.append(val)
            elif val in ")}]":
                if len(stack) == 0: return(False)
                last = stack.pop()
                if val == ")" and last == "(": continue
                elif val == "}" and last == "{": continue
                elif val == "]" and last == "[": continue
                else:
                    print("val:", val, "last:", last)
                    return(False)
        if len(stack) > 0: return(False)
        return(True)