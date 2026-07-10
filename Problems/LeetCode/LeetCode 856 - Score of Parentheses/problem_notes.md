# Problem: LC 856 — Score of Parentheses

## Problem statement
Ek balanced parentheses string di hai. Uska "score" nikalna hai in rules ke hisab se: `()` = 1; `AB` (do balanced parts side-by-side) = `score(A) + score(B)`; `(A)` (ek balanced part bracket ke andar) = `2 * score(A)`.

## Approach / strategy
Ek stack rakha jisme har entry "us particular nesting-level ka abhi tak accumulated score" represent karta hai. Stack ki shuruaat mein hi ek **base `0`** push kiya (ek "virtual base level") — taaki jab bhi poora expression khatam ho (stack sirf base tak wapas aaye), uska final score seedha stack ke us base-slot mein mil jaye, koi alag `answer` variable ki zaroorat na pade.

Har `(` par: naya level shuru, `stack.append(0)`.
Har `)` par: top pop karo — agar wo `0` tha (matlab andar kuch nahi tha, seedha `()` case), score = `1`; warna (andar kuch tha) score = `2 * top`. Ye score naye top (`stack[-1]`, jo ab parent level hai) mein add kar do.

## Attempt 1 — thinking, code, result
Poora algorithm pehle concept mein (dry-run se) derive kiya — `"(()(()))"` ko haath se trace karke `stack[-1] += score` wali line ka mechanism samjha (thoda mushkil laga pehle, "kis level pe add ho raha hai" wala confusion tha, concrete step-by-step trace se clear hua).

```python
class Solution:
    def scoreOfParentheses(self, s):
        stack = [0]
        score = 0
        for c in s:
            if c == '(':
                stack.append(0)
            else:
                if stack[-1] == 0:
                    stack.pop()
                    stack[-1] += 1
                    score = stack[-1]
                else:
                    s = 2 * stack[-1]
                    stack.pop()
                    stack[-1] += s
                    score = stack[-1]
        return score
```
Submit kiya, saare test cases pass hue pehli hi attempt mein (koi crashing bug nahi tha) — lekin do stylistic issues the.

**Issue 1 (risky, luck se bacha)**: `s = 2 * stack[-1]` — `s` function ka **input parameter tha** (poora string), lekin loop ke andar isko ek number se overwrite kar diya. Ye is baar crash nahi hua kyunki `for c in s:` pehle hi ek iterator bana chuka tha loop shuru hone par (Python ismein purana reference follow karta hai), lekin agar aage `s` ko dobara use karte to bug ban sakta tha.
- Fix: `s` ki jagah `save` naam use kiya — naming collision se bacha.

**Issue 2 (redundant, bug nahi)**: `score` variable alag se maintain kiya jaa raha tha har step mein, jabki loop khatam hone ke baad `stack[0]` khud hi final answer ban jata hai (base-level entry). `score = stack[-1]` duplicate tha dono branches mein.
- Cleanup (final):
```python
class Solution:
    def scoreOfParentheses(self, s):
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
        return stack[0]
```

## Edge case discussion (bina implement kiye, sirf socha)
Sawaal utha: agar input **invalid** ho (jaise sirf `")"`, koi matching `(` nahi) — is code ka kya hoga? Trace kiya: `stack=[0]`, `)` mile, `stack[-1]==0` True, `stack.pop()` se stack **khali** ho jata, agli line `stack[-1] += 1` **IndexError** dega (khali list pe indexing).
- Realization: algorithm ye **assume** karta hai input hamesha valid/balanced hai (jo LC 856 explicitly guarantee karta hai) — is assumption ke bahar (invalid input) crash hoga.
- Discuss kiya (implement nahi kiya, kyunki LC 856 mein zaroorat nahi thi): agar invalid-input handling chahiye hoti, to har `stack.pop()` ke baad, agle `stack[-1]` access se pehle `if stack:` check add karna padta, aur khali ho jaye to turant `return -1` (ya jo bhi convention ho) karna padta.

## Key learning
- Function parameter (`s`) ko loop ke andar overwrite karna — kabhi kabhi "chalta hai" kyunki Python ka iterator behavior bacha leta hai, lekin ye **design se bachna** hai, luck se nahi — hamesha naya, distinct variable naam use karna safer hai.
- Base/sentinel value (`stack = [0]` se shuru karna) — ye "edge case ko normal case bana dena" wala pattern hai, jo Linked-List ke dummy-node concept se directly analogous hai (khud connect kiya) — dono ka purpose same hai: special-case branching (`if stack empty` jaisa) hatana, uniform logic banana.
- Algorithm ki **assumptions** (jaise "input hamesha valid hai") explicitly pehchanna important hai — bina us assumption pe socha, edge cases (invalid input) unexpectedly crash kar sakte hain.

## Complexity
- Time: O(n) — ek pass string pe
- Space: O(n) — stack worst case (saare `(` nested) n/2 tak ja sakta hai