class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = ["+", "-", "*", "/"]
        stack = []
        total = tokens[0]
        for c in tokens:
            if c in operands:
                val2 = int(stack.pop())
                val1 = int(stack.pop())
                print(val1, c, val2)
                if c == "+":
                    total = val1 + val2
                if c == "-":
                    total = val1 - val2
                if c == "*":
                    total = val1 * val2
                if c == "/":
                    total = val1 / val2
                print(total)
                stack.append(int(total))
            else:
                stack.append(int(c))
        return int(total)