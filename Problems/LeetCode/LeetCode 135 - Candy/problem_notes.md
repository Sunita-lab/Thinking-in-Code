# Candy — GFG | LC 135

**Platform:** GFG + LeetCode  
**Difficulty:** Hard  
**Topic:** Greedy — Two Pass  
**Week:** 9 | Day 6

---

## Problem

Given `n` children with ratings, distribute minimum candies such that:
1. Every child gets at least 1 candy
2. A child with a higher rating than its neighbor gets more candy than that neighbor

---

## Greedy Strategy — Two Pass

**Why two passes?** A single left-to-right pass only satisfies the left neighbor constraint. The right neighbor constraint is missed. Two separate passes are needed — one for each direction — and the final answer takes the maximum of both at each position.

**Pass 1 (Left to Right):** If `arr[i] > arr[i-1]`, then `ans[i] = ans[i-1] + 1`. This ensures every child gets more candy than their left neighbor when their rating is higher.

**Pass 2 (Right to Left):** If `arr[i] > arr[i+1]` AND `ans[i] <= ans[i+1]`, then `ans[i] = ans[i+1] + 1`. This ensures every child gets more candy than their right neighbor when their rating is higher.

**Why the condition `ans[i] <= ans[i+1]` in Pass 2?** Pass 1 may have already set `ans[i]` to a value large enough to satisfy both constraints. Overriding it in Pass 2 without checking would break the left neighbor constraint. The condition ensures we only update when the current value isn't already sufficient — effectively taking the maximum of both passes at each position.

---

## Attempt 1 — Wrong First Pass Direction

### Thinking

Initialized `ans = [1] * n`. Tried two passes — first one going left to right, second going right to left. But the first pass condition was wrong — checking `arr[i-1] > arr[i]` (right is smaller than left) instead of `arr[i] > arr[i-1]` (current is larger than left).

### Code (with bug)

```python
class Solution:
    def minCandy(self, arr):
        ans = [1]*len(arr)
        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:  # bug — wrong direction
                ans[i] = ans[i-1] + 1
        for i in range(len(arr)-2, -1, -1):
            if arr[i] > arr[i+1] and ans[i] <= ans[i+1]:
                ans[i] = ans[i+1] + 1
        return sum(ans)
```

### Result — Sample TC passed, failed on `[1, 5, 1, 2, 3, 4]`. Output 10, expected 13.

### Bug — The "Dirty Read" Problem

`arr[i-1] > arr[i]` checks if the *previous* element is greater than current — so it was updating `ans[i]` (the right one) based on the left being bigger. But the intent was to update the *left* when current is bigger than left. Wrong element was being updated, in the wrong direction.

But there's a deeper issue — even if the condition were partially right, updating `ans[i]` based on `ans[i-1]` when `ans[i-1]` itself hasn't reached its final value yet is a **dirty read**.

**What is a dirty read here?**

In databases, a dirty read happens when you read a value that hasn't been committed yet — it might still change. The same thing happens here.

Trace on `[1, 5, 1, 2, 3, 4]` with the buggy condition:
- i=1: `arr[0]=1 > arr[1]=5`? No — nothing happens. `ans = [1,1,1,1,1,1]`
- i=2: `arr[1]=5 > arr[2]=1`? Yes → `ans[2] = ans[1] + 1 = 2`. `ans = [1,1,2,1,1,1]`

But wait — `ans[1]` is still `1` here. Later in the pass, if the code had tried to use `ans[2]` to update something, it would be using a value (`2`) that was based on `ans[1]=1` — but what if `ans[1]` was supposed to be `2`? The value `ans[2]` was computed from a "dirty" (not yet final) `ans[1]`.

**Why the correct pass avoids dirty reads:**

In the correct left-to-right pass — `if arr[i] > arr[i-1]: ans[i] = ans[i-1] + 1` — we update `ans[i]` based on `ans[i-1]`. Since we move strictly left to right, `ans[i-1]` will **never be updated again** in this pass. It is already final (committed). So reading it to compute `ans[i]` is always safe — no dirty read possible.

**Trace on `[1, 5, 1, 2, 3, 4]` with correct condition:**
- i=1: `arr[1]=5 > arr[0]=1` → `ans[1] = ans[0]+1 = 2`. `ans[0]` is final, safe to read.
- i=2: `arr[2]=1 > arr[1]=5`? No → `ans[2] = 1`
- i=3: `arr[3]=2 > arr[2]=1` → `ans[3] = ans[2]+1 = 2`. `ans[2]` is final.
- i=4: `arr[4]=3 > arr[3]=2` → `ans[4] = ans[3]+1 = 3`. `ans[3]` is final.
- i=5: `arr[5]=4 > arr[4]=3` → `ans[5] = ans[4]+1 = 4`. `ans[4]` is final.
- Result: `[1, 2, 1, 2, 3, 4]` ✅

Each value is computed from a committed left neighbor — no dirty reads.

---

## Attempt 2 — Fixed, Accepted ✅

### Thinking

Fixed the first pass condition to `arr[i] > arr[i-1]` — current element greater than left neighbor gets more candy.

### Code

```python
class Solution:
    def minCandy(self, arr):
        ans = [1]*len(arr)
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                ans[i] = ans[i-1] + 1
        for i in range(len(arr)-2, -1, -1):
            if arr[i] > arr[i+1] and ans[i] <= ans[i+1]:
                ans[i] = ans[i+1] + 1
        return sum(ans)
```

### LC 135 — same code, different function signature, accepted ✅

---

## Key Learnings

**Two pass greedy for bidirectional constraints:** When constraints exist on both sides of each element, a single pass cannot satisfy both. Two passes (left to right, then right to left) handle each direction independently, and the maximum of both gives the final answer.

**Guard condition in second pass (`ans[i] <= ans[i+1]`):**

The first pass may have already set `ans[i]` to a value large enough to satisfy the right neighbor constraint too — not just the left. Blindly overriding it in the second pass would break the first pass's work.

**Example — `[1, 2, 3, 2, 1]`:**

First pass (left to right): `[1, 2, 3, 1, 1]`
- Index 3 and 4 reset to 1 since they aren't greater than their left neighbor.

Second pass (right to left) — **without** the guard condition:
- i=3: `arr[3]=2 > arr[4]=1` → `ans[3] = ans[4]+1 = 2`. `ans = [1,2,3,2,1]`
- i=2: `arr[2]=3 > arr[3]=2` → `ans[2] = ans[3]+1 = 3`. But `ans[2]` is already `3` — no change here by coincidence.
- i=1: `arr[1]=2 > arr[2]=3`? No.
- i=0: `arr[0]=1 > arr[1]=2`? No.
- Result: `[1,2,3,2,1]` ✅ — happens to be correct here.

Now try **`[1, 3, 2, 1]`:**

First pass: `[1, 2, 1, 1]`

Second pass **without** guard:
- i=2: `arr[2]=2 > arr[3]=1` → `ans[2] = 2`. OK.
- i=1: `arr[1]=3 > arr[2]=2` → `ans[1] = ans[2]+1 = 3`. But first pass already set `ans[1]=2` correctly for the left constraint. Overriding to `3` is fine here.
- i=0: `arr[0]=1 > arr[1]=3`? No.
- Result: `[1,3,2,1]` ✅

Now try **`[1, 2, 3, 4, 3]`:**

First pass: `[1, 2, 3, 4, 1]`

Second pass **without** guard:
- i=3: `arr[3]=4 > arr[4]=3` → `ans[3] = ans[4]+1 = 2`. But first pass had `ans[3]=4`! Overriding to `2` **breaks** the left constraint — index 3 has rating 4, but now gets fewer candies than index 2 (rating 3, candies 3).
- Result: `[1,2,3,2,1]` ❌ — wrong!

Second pass **with** guard (`ans[i] <= ans[i+1]`):
- i=3: `arr[3]=4 > arr[4]=3` AND `ans[3]=4 <= ans[4]=1`? No — `4 > 1`, condition fails. `ans[3]` stays `4`. ✅

Result: `[1,2,3,4,1]` — but wait, now index 3 (candies 4) > index 4 (candies 1) with rating 4 > 3. ✅

The guard condition ensures: **only update if the current value isn't already sufficient.** This is effectively taking the element-wise maximum of both passes without explicitly computing it. Intuition: "first pass might have already fixed some positions correctly — don't break them."

---

## Complexities

| | Time | Space |
|---|---|---|
| Attempt 1 | O(n) | O(n) |
| Attempt 2 | O(n) | O(n) |

**Time:** Two O(n) passes — O(n) total.  
**Space:** O(n) for the `ans` array.