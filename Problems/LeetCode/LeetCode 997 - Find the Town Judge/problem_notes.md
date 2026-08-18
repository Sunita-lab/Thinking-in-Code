# Problem: Find the Town Judge (LC 997)

**Week 16 — Day 2 — Degree & Basic Queries (extra LC practice)**

## Problem Statement
`n` log hain, `trust` list di gayi hai jahan `trust[i] = [a, b]` matlab `a` trusts `b`. Town judge wo person hai jise **sabne trust kiya ho** lekin **wo khud kisi ko trust na kare**. Judge ka number return karo, warna `-1`.

## My Approach — 3 attempts (full journey)

### Attempt 1 (WRONG — source/target confusion)
```python
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        out = []
        In = []
        if trust:
            for t in trust:
                out.append(t[0])
                In.append(t[1])
            inset = set(In)
            diff = [x for x in out if x not in inset]
            if len(diff) == 1:
                return diff[0]
        return -1
```
**Bug**: `diff` nikala "out mein se jo In mein nahi hai" — ye galat direction thi. Judge ke liye chahiye tha koi aisa vertex jo **In mein ho lekin out mein na ho** (sab usse trust karte hain, wo kisi ko trust nahi karta). Maine source aur target ka role confuse kar diya.

### Attempt 2 (CORRECT but inefficient)
```python
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        out = []
        In = []
        if trust:
            for t in trust:
                out.append(t[0])
                In.append(t[1])
            maxin = max(set(In), key=In.count)
            outset = set(out)
            if In.count(maxin) == n-1 and maxin not in outset:
                return maxin
            return -1
        return n if n == 1 else -1
```
Logic sahi tha — `In` mein sabse zyada frequent element dhundha (candidate judge), verify kiya ki wo `n-1` baar aata hai (sab trust karte hain) aur `outset` mein nahi hai (khud kisi ko trust nahi karta). **Accepted**, lekin inefficient — `max(set(In), key=In.count)` mein har unique element ke liye `.count()` call hoti hai jo khud O(n) hai, isliye total worst-case time O(n²) ban jaata hai (jab unique elements bhi n ke order ke ho).

### Attempt 3 (OPTIMAL — array-based frequency counting)
```python
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        outs = [0]*n
        ins = [0]*n
        if trust:
            for t in trust:
                outs[t[0]-1] += 1
                ins[t[1]-1] += 1
            maxin = max(ins)
            idx = ins.index(maxin)
            if maxin == n-1 and outs[idx] == 0:
                return idx + 1
            return -1
        return 1 if n == 1 else -1
```
Same "Degree for each vertex" pattern jo aaj hi solve kiya tha — `ins`/`outs` arrays (size n) mein directly index se count track kiya, `.count()` ki repeated calls avoid ki.

## (1) Mid-way doubts
- **Attempt 1 ka bug**: `out` aur `In` lists mein confusion — kisme kya check karna hai (source vs target) — ye conceptually clear nahi tha shuru mein ki judge "In mein present, out mein absent" hona chahiye.
- **Attempt 2 se Attempt 3 tak ka trigger**: Claude ne pucha `max(..., key=In.count)` ki actual complexity kya hai — trace karke realize hua ki `.count()` andar se O(n) hai aur `max` usse har unique element ke liye call karta hai, isliye hidden O(n×k) cost hai jo worst case O(n²) tak ja sakti hai. Concise-looking code hamesha efficient nahi hota.

## (2) Syntax / Python concepts touched
- `max(iterable, key=function)` — samjha ki `key` function har element ke liye call hoti hai, aur agar wo function khud costly hai (jaise `.count()`), to total complexity multiply ho jaati hai.
- List indexing with offset (`t[0]-1`) — jab values 1-indexed hon (`trust` mein 1 se n tak) lekin array 0-indexed ho.

## (3) Key insight / key learning
**"Jab keys ek known, continuous range mein ho (jaise 1 se n), to hashmap/dictionary ke bajaye seedha array/list use karo — index hi key ban jaata hai, access O(1) hota hai bina hashing/counting overhead ke."**

Ye general optimization pattern hai jo already "Degree for each vertex" problem mein use hua tha (aaj hi), aur yahan explicitly realize hua ki ye ek reusable technique hai — jab bhi values ek bounded range mein predictable hon, array-based counting dictionary/`.count()`-based approach se better hoga, dono speed aur simplicity mein.

## Time & Space Complexity
| Attempt | Time | Space |
|---|---|---|
| Attempt 1 (buggy) | O(E) but wrong logic | O(E) |
| Attempt 2 (correct, inefficient) | O(n×k) worst case O(n²) | O(E) |
| Attempt 3 (optimal) | O(n + E) | O(n) |

## Connections to earlier learning
- Direct reuse of "Degree for each vertex" (GFG, solved same day) pattern — array-indexed frequency counting instead of dictionary/count-based approach.
- Debugging journey highlights importance of correctly identifying source vs target when dealing with directed relationships (trust[a][b] = a trusts b, similar to edges[u][v] = u -> v from earlier problems).