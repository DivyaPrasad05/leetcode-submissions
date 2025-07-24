class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')': '(', ']': '[', '}':'{'}

        if len(s) % 2 != 0:
            return False

        for char in s:
            if char in closeToOpen:
                corr = closeToOpen[char]
                if not stack:
                    return False
                openBracket = stack.pop()
                if corr != openBracket:
                    return False
            else:
                stack.append(char)

        return not stack
