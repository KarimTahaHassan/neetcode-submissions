class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        for i in range(len(s)):
            if s[i] not in closeToOpen:
                stack.append(s[i])
            elif stack and closeToOpen[s[i]] == stack[-1]:
                stack.pop()
                continue
            else:
                return False

        if len(stack) > 0:
            return False
        return True
            