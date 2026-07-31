class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for e in s:
            if e in ('(','{','['):
                stack.append(e)
            elif not stack and e in (')', '}', ']'):
                return False
            elif stack[-1] == '(' and e == ')':
                stack.pop()
            elif stack[-1] == '{' and e == '}':
                stack.pop()
            elif stack[-1] == '[' and e == ']':
                stack.pop()
            else:
                return False
        if stack:
            return False
        return True

            

        