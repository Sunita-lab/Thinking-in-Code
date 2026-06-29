# Week 9 — Day 1 | Greedy Problems

---

## Problem 1 — Minimum Number of Coins (GFG)

**Platform:** GFG  
**Topic:** Greedy — Basic  
**Coins available:** `[1, 2, 5, 10]`  
**Goal:** Minimum coins to make amount `n`

---

### Attempt 1 — Hardcoded Division

**Thinking:**
- Strategy sahi thi — sabse bada coin pehle lo, remainder nikalo, aage badho
- But implementation mein coins ko hardcode kar diya — `n//10`, `n//5`, `n//2`, `n%2`

**Code:**
```python
class Solution:
    def findMin(self, n):
        tens = (n//10)
        n %= 10
        fives = (n//5)
        n %= 5
        twos = (n//2)
        ones = n%2
        return tens + fives + twos + ones
```

**Result:** All TC pass (1120/1120)

**Bug/Limitation:**
- Logically correct but **not greedy** — koi rule nahi hai yahan, sirf hardcoded math hai
- Generalized nahi hai — agar coins `[1, 2, 5, 10]` na hote toh kaam nahi karta
- Greedy ka matlab hai — ek rule banao aur us rule pe loop chalao; yahan loop hai hi nahi

---

### Attempt 2 — Generalized Greedy

**Thinking:**
- Pehle attempt ki limitation samajh aayi — hardcoded hai, greedy nahi
- Sahi approach: coins ko sort karo descending, sabse bada coin pehle lo, remainder pe aage badho
- Loop chalao jab tak `n != 0`
- Har iteration mein `max(coins)` lo, count badhao, remainder nikalo, us coin ko list se hata do

**Code:**
```python
class Solution:
    def findMin(self, n):
        coins = [1, 2, 5, 10]
        count = 0
        while n != 0:
            div = max(coins)
            count += n // div
            n = n % div
            coins.remove(div)
        return count
```

**Result:** All TC pass (1120/1120)

**Why greedy works here:**
- Coins `[1, 2, 5, 10]` mein har bada coin chhote ka multiple hai
- Isliye sabse bada coin pehle lena safe hai — future choices kharab nahi hoti
- Ek choice dusri choice ko disturb nahi karti — greedy choice property hold karti hai

---

### Complexities

| | Time | Space |
|---|---|---|
| Attempt 1 | O(1) | O(1) |
| Attempt 2 | O(n/min_coin) | O(1) |

> Note: Attempt 2 ka time O(n/min_coin) isliye — worst case mein sab 1s se banana padega. Coins ki list fixed size hai toh uska contribution constant hai.

