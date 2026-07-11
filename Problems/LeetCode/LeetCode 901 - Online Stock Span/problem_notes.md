# Problem: Stock Span (GFG) + LC 901 — Online Stock Span

## Problem statement
Har din stock ka price aata hai. Us din ka "span" = kitne consecutive din pehle (aaj ka din bhi count karke) tak stock price aaj ke price se **kam ya equal** raha, jab tak koi din mile jaha price aaj se zyada tha (wahan span ruk jata hai).

GFG variant: poora array ek saath diya hai, saare din ka span ek saath return karna hai.
LC 901 variant: "streaming/online" — ek `StockSpanner` class banani hai jiska `next(price)` method ek din ek baar call hota hai, turant us din ka span return karta hai (poora array pehle se pata nahi hota).

## Approach / strategy
Core insight: ye **Previous Greater Element** ka hi application hai. Span = `currentIndex - prevGreaterIndex` (jaha prevGreaterIndex na mile to `-1` maan lo, formula `currentIndex - (-1) = currentIndex + 1` ban jata).

## Part 1 — GFG (array-based)

### Derivation
Pehle manually kai examples trace kiye (`[100,80,60,70,60,75,85]`) taaki span ka pattern samajh aaye. Phir socha — baar-baar peeche traverse karne ke bajaye, agar "Previous Greater ka index" pata ho, to span seedha subtraction se nikal sakta hai. Formula khud derive kiya, `+1` galti se pehle add kiya tha, phir concrete examples se (jaise `85` ka span `6`, `70` ka span `2`) verify karke `+1` hataya — sahi formula: `span = currentIndex - prevGreaterIndex` (with `-1` sentinel jab kuch na mile).

### Attempt 1 — pehla poora khud likha
```python
stack = [0]
spans = [1]*len(arr)
for i in range(1, len(arr)):
    while arr[stack[-1]] <= arr[i]:
        stack.pop()
    spans[i] = i - stack[-1]
    stack.append(i)
```
Structure genuinely accha tha (pehli koshish mein khud, bina step-by-step guide ke) — lekin do **empty-stack crash risks** miss hue:
- **Bug A**: `while arr[stack[-1]] <= arr[i]:` — agar saare elements pop ho jayen (koi bhi purana element `arr[i]` se bada na ho), `stack` khali ho sakta hai beech mein, aur agli check `arr[stack[-1]]` crash karti (IndexError).
- **Bug B**: `spans[i] = i - stack[-1]` — agar `while` loop ke baad `stack` khali reh jaye (koi Previous Greater nahi mila), ye bhi crash karega.

### Fix (evolution)
Pehla fix attempt: `if not stack:` ka special block loop ke shuru mein add kiya (sirf `i=0` ke liye) — lekin ye sirf **outer** empty-case cover karta tha, `while` loop ke **andar** (beech mein khali hone wala) case abhi bhi crash kar sakta tha.

Doosra fix: `while` condition mein bhi `stack and` add kiya, aur `spans[i]` line mein ternary (`if stack else ...`) add kiya. Pehle fallback value `1` rakhi thi (galat — sirf `i=0` ke liye sahi thi), phir realize kiya ki general formula `i - (-1) = i+1` chahiye — fallback ko `1+i` kiya.

### Cleanup — redundant block hataya
Realization hui ki `if not stack:` wala special block ab **redundant** hai — kyunki `while stack and ...` (jo empty-check khud kar leta hai) aur ternary ka `else` branch (jo `i+1` deta hai) **already** `i=0` ka case bhi sahi handle kar dete hain. Special-case block hata diya — ye wahi pattern tha jo Score-of-Parentheses ke sentinel-value discussion mein bhi dekha tha: jab general conditions sahi design ki jayein, special-case branching apne aap unnecessary ho jati hai.

### Final (GFG)
```python
class Solution:
    def calculateSpan(self, arr):
        stack = []
        spans = [1]*len(arr)
        for i in range(len(arr)):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
            spans[i] = i - stack[-1] if stack else i + 1
            stack.append(i)
        return spans
```
Submit kiya, saare test cases pass hue.

## Part 2 — LC 901 (streaming/online version)

### Naya challenge — poora array available nahi hai
LC 901 mein `next(price)` ek din ek baar call hota hai — koi poora `arr` nahi hai jisme index se access karein. Realization: **index ki zaroorat hi khatam ho sakti hai** agar stack mein index ki jagah seedha **`(price, span)` ka pair** rakha jaye — jab koi purana element pop ho, uska span "absorb" kar liya jaye naye span mein.

### Derivation
```
next(price):
    span = 1
    while stack and stack[-1].price <= price:
        (_, oldSpan) = stack.pop()
        span += oldSpan   # purane din ka span bhi is naye span mein absorb ho gaya
    stack.push((price, span))
    return span
```
Concrete trace kiya `[100,80,60,70]` pe — `70` ke liye `60` pop hote waqt uska span (`1`) absorb hua, final span `2` bana — match hua GFG wale answer se, bina kisi index ke.

### Attempt — bug
```python
def next(self, price: int) -> int:
    span = 1
    while self.stack and self.stack[-1][0] <= price:
        _, oldSpan = self.stack.pop()
        span += oldSpan
        self.stack.append((price, span))   # <-- yahan bug
    return span
```
**Bug**: `self.stack.append((price, span))` galti se `while` loop ke **andar** reh gaya (indentation). Is se har baar jab loop chalta (har purane element ke pop hone par), naya `(price, span)` **turant** push ho jata — agar loop multiple baar chalta, stack mein **usi price ki multiple/duplicate entries** ban jati.

### Fix
`append` line ko `while` loop ke **bahar** nikala, `return` se pehle — taaki poora loop khatam hone ke baad (saare zaroori pops ho chuke, final span ban chuka), sirf **ek baar** push ho.
```python
class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            _, oldSpan = self.stack.pop()
            span += oldSpan
        self.stack.append((price, span))
        return span
```
Submit kiya, accepted.

## Special Learning — "Class state maintain karna" (jo stumble karata hai)

Ye poori OOP nahi hai — sirf ek chhota, specific pattern hai jo baar-baar LeetCode class-based problems mein aata hai (Min Stack LC 155, StockSpanner LC 901, jaise problems).

### Pattern kya hai
Do hisse hote hain:
1. **`__init__(self)`** — jab object banta hai (`spanner = StockSpanner()`), ye **ek baar** chalta hai. Yahan **starting state** define hoti hai — jaise `self.stack = []`. `self.` lagana zaroori hai taaki ye data **object ke saath permanently jud jaye**, sirf `__init__` ke andar hi na reh jaye (jaise Day 1 mein seekha tha).
2. **Doosre methods** (`next`, `push`, `pop`, etc.) — ye **baar baar** call hote hain (`spanner.next(100)`, phir `spanner.next(80)`, ...). Har call mein `self.stack` **wahi purana state** hai jo pichli call ne chhoda tha — matlab data **persist** karta hai calls ke beech, kyunki `self.` se object ke saath attach hai.

### Kyu confusing lagta hai
Normal function (jaise `def solve(arr):`) mein har call **fresh/independent** hoti hai — koi memory nahi rehti pichli call ki. Class-state wale pattern mein, **methods ek doosre se "connected" hote hain** `self` ke through — ye ek naya mental model hai jo normal function-calling se alag hai.

### Test — kaise pehchane ki ye pattern hai
Agar problem statement mein diya ho:
- `["ClassName", "methodA", "methodB", ...]` jaisa call-sequence, ya
- "design a class that supports these operations", ya
- Ek method baar baar call hoga aur **pichli calls ka result yaad rakhna** hai (jaise yahan span accumulate karna, ya Min Stack mein minimum track karna)

— to ye "class state maintain karna" wala pattern hai. Solution structure hamesha:
```python
class SomeName:
    def __init__(self):
        self.data = ...   # starting state, self. zaroori

    def someMethod(self, ...):
        # self.data ko read/modify karo
        # ye modification agli call mein bhi dikhega
```

### Is course mein jaha jaha ye pattern pehle aa chuka hai
- Day 1 — Stack (array + LL) ka `myStack` class
- Day 3-4 — `kStacks` class
- Day 5 — `SpecialStack` (Min Stack)
- Day 9 — `StockSpanner`

Har baar core confusion same tha — `self.` kaha lagana hai, aur ye samajhna ki `__init__` sirf ek baar chalta hai jabki baaki methods baar-baar. Formal OOP (inheritance, polymorphism, encapsulation ke deeper rules) is course mein abhi tak nahi aaya — jo chahiye tha wo sirf itna tha: **`self.` object ke saath data ko methods ke beech persist karta hai** — jo incrementally, real problems se hi seekha ja raha hai.

## Complexity (dono versions)
- **GFG**: Time O(n) amortized (har element max ek push, ek pop), Space O(n)
- **LC 901**: `next()` ek call ka time O(1) amortized (har price max ek push, ek pop poore lifetime mein), Space O(n) worst case