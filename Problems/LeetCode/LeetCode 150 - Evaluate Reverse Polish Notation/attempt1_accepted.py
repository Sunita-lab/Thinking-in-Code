class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ['+', '-', '*', '/']
        def operation(num1, num2, c):
            if c == '+':
                return num1 + num2
            elif c == '-':
                return num1 - num2
            elif c == '*':
                return num1 * num2 
            else:
                return int(num1 / num2)           
        stack = []
        for c in tokens:
            if c not in ops:
                stack.append(int(c))
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                stack.append(operation(num1, num2, c))
        return stack[0]        


        