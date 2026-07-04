# Problem: LC 20 — Valid Parentheses
### Solution Link - https://leetcode.com/submissions/detail/2056055864/

## Problem statement
Sirf `(`, `)`, `{`, `}`, `[`, `]` wali string di hai. Check karo ki brackets valid/balanced hain — har opening bracket ka sahi type ka closing bracket sही order mein aaya ho.

## Approach / strategy
Pehla initial idea tha "leftmost aur rightmost ko ek saath match karo" — ye `()[]` jaise cases pe **fail** ho gaya (leftmost `(`, rightmost `]`, seedha match nahi karte, jabki string valid hai). Isse realization hui ki matching **position (left/right end)** se decide nahi hota, balki **"sबसे recent unclosed opening bracket"** se decide hota hai — yahi stack (LIFO) ka use case hai.

Final approach:
1. Opening bracket → push
2. Closing bracket → stack khali hai to invalid; warna top pop karke check karo match hota hai ki nahi
3. End mein stack empty honi chahiye (valid ke liye)

## Attempt 1 — thinking, code, result, bugs
```python
class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')':'(', ']':'[', '}':'{'}
        arr = []
        i = 0
        while i < len(s):
            if s[i] in mapping.values():
                arr.append(s[i])
            else:
                if arr and arr[-1] == mapping[s[i]]:
                    arr.pop()
                else:
                    return False
            i += 1        
        return True if not arr else False    
```
Sab test cases pass hue pehli hi clean attempt mein logic ke hisab se, lekin ek pehli draft mein (jo submit nahi hui thi) `return True` seedha end mein tha bina `if not arr` check ke — us wajah se `"["` jaisa case (sirf unclosed opening) galat True de rahaहोता, kyunki koi crash nahi hota tha traversal mein, lekin end-state check missing tha.

## Mapping direction ka experience
Pehle `opening: closing` map kiya tha (jaise `{'(' : ')'}`). Realization hui ki jab stack ke top element (jo ek **opening bracket** hai) ka match dhundhna hota hai current **closing bracket** ke against — dict mein **value se key dhundhna** direct/efficient nahi hota Python mein (reverse lookup karna padta O(n) mein). Isliye mapping **flip** ki — `closing: opening` — taaki current closing bracket ko key banake seedha O(1) mein uska matching opening mil jaye, jise stack ke top se compare karna hai.

## Stylistic note
`while i < len(s)` aur manual `i += 1` use kiya tha index ke liye — lekin is problem mein index ki actual value kabhi zaroori nahi thi, sirf character-by-character dekhna tha. `for char in s` zyada clean hota — is realization ke baad aage jab bhi sirf elements pe iterate karna ho (index ki zaroorat na ho), `for` loop directly use karna.

## Key learning
- Matching ka concept "position" se nahi, "order of occurrence / recency" se decide hota hai → stack fit baithta hai.
- Dict mapping ki direction is baat pe depend karti hai ki lookup **kis direction mein** karna hai — jis cheez se dusri cheez dhundhni hai, wahi key honi chahiye.
- Loop ke end-state ko explicitly check karna zaroori hai (sirf traversal ke andar bugs na hona kaafi nahi, "poori string process hone ke baad stack ki state kya hai" bhi check karna hai).

## Complexity
- Time: O(n) — ek pass string pe
- Space: O(n) — worst case sabhi opening brackets stack mein