class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = 0
        stack = []
        for e in operations:
            if e not in ('+', 'D', 'C'):
                stack.append(e)
            elif e == '+' and len(stack) >= 2:
                tmp = int(stack[-1]) + int(stack[-2])
                stack.append(tmp)
            elif e == 'D':
                tmp = int(stack[-1]) * 2
                stack.append(tmp)
            elif e == 'C':
                stack.pop()
        for e in stack:
            ans += int(e)
        return ans
            
        