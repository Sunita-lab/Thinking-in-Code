# Problem: LC 150 — Evaluate Reverse Polish Notation

## Problem statement
Tokens ki list di gayi hai jo postfix (Reverse Polish) notation mein hai (jaise `["2","3","4","*","+"]`). Isko evaluate karke final integer answer return karna hai.

## Approach / strategy
Wahi mechanical postfix-evaluation rule use kiya jo concept mein derive kiya tha: number mile → push; operator mile → top se do pop karo (jo baad mein push hua wo pehla operand hoga calculation ke liye order ke hisab se), apply karo, result push karo wapas. End mein stack mein sirf ek element bachega — wahi answer.

## Attempt 1 — thinking, code, result, bug
```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ['+', '-', '*', '/']
        def operation(num1, num2, c):
            if c == '+': return num1 + num2
            elif c == '-': return num1 - num2
            elif c == '*': return num1 * num2
            else: return num1 // num2
        stack = []
        for c in tokens:
            if c not in ops:
                stack.append(c)
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                stack.append(operation(num1, num2, c))
        return stack[0]
```
Zyada test cases pass hue, lekin ek case fail hua jahan input sirf `["18"]` tha (single operand, koi operator hi nahi).

**Bug 1 — negative division**: `//` Python mein **floor division** karta hai (neeche ki taraf round, jaise `-7 // 2 = -4`), lekin LeetCode expects **truncation towards zero** (`-7 / 2` → `-3`), jo normal integer division convention hai (C++/Java jaisa). Fix: `int(num1 / num2)` — true division karke phir `int()` se truncate karna (zero ki taraf).

**Bug 2 — single operand case fail**: jab input sirf `["18"]` tha (koi operator use hi nahi hua), `stack.append(c)` se **string** `"18"` push hoती thi, aur `return stack[0]` string return karta — jabki function ko integer return karna chahiye tha. Type mismatch se test case fail hota. Fix: push time pe hi `stack.append(int(c))` — operand ko turant integer bana diya, chahe operator use ho ya na ho baad mein.

## Fix (final)
```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ['+', '-', '*', '/']
        def operation(num1, num2, c):
            if c == '+': return num1 + num2
            elif c == '-': return num1 - num2
            elif c == '*': return num1 * num2
            else: return int(num1 / num2)
        stack = []
        for c in tokens:
            if c not in ops:
                stack.append(int(c))
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                stack.append(operation(num1, num2, c))
        return stack[0]
```
Note: operator branch mein `int(stack.pop())` ab technically redundant hai (kyunki push time pe hi int bana diya tha), lekin harmless hai — double conversion, no functional issue.

## Key learning
- `//` (floor division) aur "truncate towards zero" **alag** hain, especially negative numbers ke case mein — LeetCode/most languages standard integer division truncate karta hai, floor nahi.
- Edge case jahan koi operator hi na ho (single-token input) — ye zaroor test karna chahiye, kyunki type conversion ka missing step tabhi surface hota hai jab operator branch bilkul chalta hi nahi.
- Operand ko **push karte waqt hi** correct type mein convert karna better practice hai, "baad mein jab zaroorat pade tab convert karunga" se kam bugs aate hain.

## Complexity
- Time: O(n)
- Space: O(n)