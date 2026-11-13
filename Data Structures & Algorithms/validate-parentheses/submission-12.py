class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            else:
                if not stack:
                    return False
                popped = stack.pop()
                if char == ")" and popped != "(":
                    return False
                if char == "}" and popped != "{":
                    return False
                if char == "]" and popped != "[":
                    return False
        
        return not stack 