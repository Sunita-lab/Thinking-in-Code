class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        stack = [0]
        for c in s:
            if c == '(':
                stack.append(0)
            else:
                if stack[-1] == 0:
                    stack.pop()
                    stack[-1] += 1
                else:
                    save = stack[-1] * 2
                    stack.pop()
                    stack[-1] += save
                score = stack[-1]
        return score                   
        