# LC 643 — Maximum Average Subarray I

*Date: 12 May 2026 | Attempt 1*

---

## Problem

Given an array `nums` and integer `k`, find the contiguous subarray of length `k` with the maximum average. Return that average.

```
Input:  nums = [1, 12, -5, -6, 50, 3], k = 4
Output: 12.75 (Failed sample test case on LeetCode, got 12.00)
```

---

## Attempt 1 — Journey

### Pehla approach (galat direction)

Har step pe `/k` karte jaao — average directly track karo:

```python
current_avg = 0.00
for i in range(k):
    current_avg += nums[i] / k

for i in range(len(nums) - k):
    current_avg = current_avg - nums[i]/k + nums[i+k]/k
```

**Kya hua:** Logic sahi thi, par floating point error accumulate hoti hai har division pe. Chhote inputs pe kaam karta tha, edge cases pe nahi.

---

### Dusra approach — fix ki

Sum pehle rakho, end mein ek baar divide karo:

```python
current_sum = sum(nums[:k])
max_avg = current_sum / k

for i in range(len(nums) - k):
    current_sum = current_sum - nums[i] + nums[i+k]
    current_avg = current_sum / k
    max_avg = max(current_avg, max_avg)

return max_avg
```

**VS Code pe:** Sahi answer aa raha tha — 12.75. LeetCode pe wrong answer.

---

## Resistance 1 — Wrong Answer on LeetCode (same logic, different output)

**Kya hua:** VS Code pe 12.75 aa raha tha. LeetCode pe 12.00 aa raha tha.

**Investigation:** Print statements lagaye, manually trace kiya — code bilkul sahi tha.

**Root cause:** LeetCode pe `class Solution(object)` select kiya tha — yeh Python 2 hai.

Python 2 mein:
```python
integer / integer = integer   # floor division
2 / 4 = 0                     # Python 2
2 / 4 = 0.5                   # Python 3
```

`current_sum` integer tha — toh `/k` se floor division ho rahi thi.

**Fix:**
- Python 3 select karo LeetCode pe (`class Solution:`)
- Ya Python 2 mein `float(k)` karo — ek operand float hone se division float ho jaati hai

---


## Final Accepted Code

```python
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = sum(nums[:k])
        max_avg = current_sum / k

        for i in range(len(nums) - k):
            current_sum = current_sum - nums[i] + nums[i + k]
            current_avg = current_sum / k
            max_avg = max(current_avg, max_avg)

        return max_avg
```

---

## Key Learnings

**1. Sum pehle, divide baad mein**
Floating point errors avoid karne ke liye — division sirf end mein, ek baar.

**2. Python 2 vs Python 3**
LeetCode pe hamesha Python 3 select karo. `class Solution(object)` = Python 2.

**3. Loop range vs window count**
`n - k + 1` aur `n - k` alag cheezein hain — dono ka matlab samajhna zaroori hai.


---

## Attempt Log

| Attempt | Date | Status | Notes |
|---|---|---|---|
| Attempt 1 | May 2026 | ✅ Accepted | Python 2/3 issue, float division resistance aayi |

---

*Resistance = learning. Smooth nahi tha — isliye yaad rahega.*