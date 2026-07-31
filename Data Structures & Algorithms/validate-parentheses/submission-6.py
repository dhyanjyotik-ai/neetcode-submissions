class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'}':'{', ')':'(', ']':'['}
        for e in s:
            if e in ('(', '{', '['):
                stack.append(e)
            elif not stack or stack[-1] != pairs[e]:
                return False
            else:
                stack.pop()         
        return not stack


            

        