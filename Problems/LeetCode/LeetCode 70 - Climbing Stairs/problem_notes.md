# Climbing Stairs — LC 70

**Source**: LeetCode 70 (LC Exclusive — Fibonacci pattern recognition problem)
**Topic**: Recursion & Backtracking — Week 12, Day 1
**Status**: Solved independently (naive recursion, no hints for core logic) → hit TLE → fixed with memoization independently

---

## Problem Statement

`n` steps chadhne hain. Ek baar mein **1 ya 2 steps** liye ja sakte hain. Total kitne **distinct ways** hain top (step n) tak pahunchne ke?

**Constraint**: `1 <= n <= 45`

---

## Approach — Thinking Process

### Step 1: Last step se reasoning

Socha gaya: agar main step `n` (top) pe khadi hun, main wahan **kahan se aayi** ho sakti hun? Sirf 2 possibilities:
- Step `n-1` se ek step chadhke
- Step `n-2` se do steps chadhke

Ye do raaste **mutually exclusive** hain (ya toh ek se aaogi, ya doosre se — dono se nahi).

### Step 2: P&C connection (self-derived)

Jab do mutually exclusive raaste hote hain kisi state tak pahunchne ke, unke count **add** hote hain — ye combinatorics ka OR-rule hai ("OR situations mein add karo, AND situations mein multiply karo").

Isse recurrence bani: `ways(n) = ways(n-1) + ways(n-2)`

**Key realization (self-articulated)**: Fibonacci mein recurrence *definition* se aayi thi (`fib(n)=fib(n-1)+fib(n-2)` seedha diya hota hai). Yahan wahi recurrence *reasoning se emerge* hui — definition se nahi. Isliye bahut saare alag-looking problems Fibonacci pattern follow karte hain: jab bhi "kisi state tak exactly 2 mutually-exclusive raaste hain jo pichhli 2 states se aate hain", Fibonacci recurrence emerge hoga.

### Step 3: Base cases

- `n=1` → sirf 1 way (single 1-step)
- `n=2` → 2 ways (1+1, ya seedha 2)

---

## Attempt 1 — Naive Recursion

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)
```

**Result**: Logic correct tha (verified: n=3 → climbStairs(2)+climbStairs(1) = 2+1 = 3 ✓), lekin **TLE** — 44/44 test cases mein sirf 21 pass hue, **n=44 pe fail**.

### Bug Diagnosis (self-driven)

- Same issue jo Fibonacci mein discuss hui thi — overlapping recursive calls, exponential blow-up
- Constraint check kiya: `n` max 45 tak jaata hai
- n=44 ke liye total calls ≈ `2×fib(45)-1` — crores mein, isliye time limit cross

---

## Attempt 2 — Memoization (self-implemented)

```python
class Solution:
    def __init__(self):
        self.memo = {1: 1, 2: 2}
    
    def climbStairs(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        else:
            self.memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            return self.memo[n]
```

**Result**: Passed. Har `climbStairs(k)` ab sirf **ek baar** compute hota hai — O(2ⁿ) se **O(n)** time complexity.

### Key Design Choice — `self.memo` (why not local variable)

**Self-reasoned**: agar memo ko local variable ki tarah function ke andar banaya hota (`memo = {}` seedha andar), har recursive call apna **naya local** memo banati — Python mein har call ka apna scope hota hai (same principle jo pehle `counting()` problem mein dekha tha, Day 1 ka pehla sum-of-n problem). Sharing hi nahi hoti, memoization ka fayda khatam.

`self.memo` ka use karke — `self` ka matlab "is particular object ka data". Saari recursive calls (`self.climbStairs(n-1)`, etc.) **same object** pe ho rahi hain, isliye sab ek hi `self.memo` dictionary ko access/update karte hain → sharing ho paati hai across saari calls.

Base cases (`{1:1, 2:2}`) directly memo mein pre-filled kiye — separate `if` check ki zaroorat nahi padi.

---

## Key Learnings

1. **Fibonacci recurrence recognize karna reasoning se, definition se nahi**: jab bhi "state X tak pahunchne ke exactly 2 mutually-exclusive raaste, jo pichhli 2 states se aate hain" — Fibonacci pattern hoga, chahe problem statement mein Fibonacci ka naam kahin na ho.

2. **Naive recursion + no memo = exponential blow-up hoga wherever overlapping subproblems hain** — chahe problem "Fibonacci" na kehlaye. Pattern spot karna hi important hai, naam nahi.

3. **Memoization ka practical trigger**: TLE dekh ke turant connect kiya "ye wahi issue hai jo hum Fibonacci mein discuss kar chuke hain" — cross-problem pattern recognition achha tha.

4. **`self.X` vs local variable — shared state ka concept**: ye distinction bahut important hai jab bhi recursive calls ke beech data share karna ho (memo tables, counters, visited sets — sab backtracking mein baar baar aayega).

---

## Complexity

**Naive (Attempt 1)**:
- Time: O(2ⁿ) — exponential, overlapping subproblems
- Space: O(n) — recursion stack depth

**Memoized (Attempt 2)**:
- Time: O(n) — har state ek hi baar compute
- Space: O(n) — memo dictionary + recursion stack

---

## Connection to Broader Pattern

Day 1 ka teesra problem jahan recursive calls **dependent/overlapping** the (Fibonacci jaisa) — Tower of Hanoi ke independent calls se contrast. Ye problem confirm karta hai ki overlapping-subproblem issue sirf "named" Fibonacci tak limited nahi hai — koi bhi problem jiski recurrence structure similar ho, wahi TLE risk carry karta hai, aur wahi memoization fix apply hota hai.

Memoization abhi sirf concept-level tool hai yahan — **DP week** mein iska full treatment (top-down vs bottom-up, tabulation, space optimization) hoga.