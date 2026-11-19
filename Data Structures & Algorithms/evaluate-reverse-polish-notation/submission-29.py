class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char == "+" or char == "-" or char == "*" or char == "/":
                if char == "+":
                    temp = stack[-1] + stack[-2]
                    stack.pop()
                    stack.pop()
                    stack.append(temp)
                elif char == "-":
                    temp = stack[-2] - stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(temp)
                elif char == "*":
                    temp = stack[-1] * stack[-2]
                    stack.pop()
                    stack.pop()
                    stack.append(temp)
                elif char == "/":
                    temp = stack[-2] / stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(int(temp))
            else:
                stack.append(int(char))

        return int((stack[-1]))