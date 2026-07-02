# Stock Buy and Sell (Multiple Transactions) — GFG + LC 122

**Platform:** GFG + LeetCode  
**Difficulty:** Medium  
**Topic:** Greedy  
**Week:** 9 | Day 5

---

## Problem

Given an array of stock prices where `arr[i]` is the price on day `i`, find the maximum profit that can be earned by buying and selling the stock multiple times. At most one stock can be held at a time — must sell before buying again.

---

## Greedy Strategy (Derived)

Every time the price goes up from one day to the next, that increase is profit. Add all consecutive positive differences. Skip days where price drops.

**Why this works:** Any multi-day holding strategy (buy on day 1, sell on day 5) gives the same result as collecting every small consecutive gain along the way. Example — `[1, 3, 5]`: holding from day 1 to day 3 gives profit 4. Buying at 1, selling at 3 (profit 2), buying at 3, selling at 5 (profit 2) also gives 4. The sum of consecutive differences always equals the total gain of any longer hold.

---

## Attempt 1 — Over-engineered, Wrong Output

### Thinking

The constraint "at most one stock held at a time" felt very important — seemed like tracking buy/sell state explicitly was necessary. Used a `sell` flag to track whether stock was currently held. When price increased from `buy` day, added profit and reset buy. When price dropped and `sell` was True, updated buy to current day.

### Code

```python
class Solution:
    def stockBuySell(self, arr):
        n = len(arr)
        buy = 0
        sell = False
        profit = 0
        i = 1
        while i < n:
            if not sell:
                if arr[i] >= arr[buy]:
                    sell = True
                    profit += arr[i] - arr[buy]
                    if i+1 < n and arr[i+1] > arr[i]:
                        buy = i
                        sell = False
            else:
                buy = i
                sell = False
            i += 1
        return profit
```

### Result — 0/TC passed. Failed on `[63, 17, 59, 6, 8, 7, 52, 50, 20]`, output 0, expected 89.

### Bugs

**Bug 1 — `>=` instead of `>`:** Same price on consecutive days gives 0 profit but still triggered the sell logic, resetting buy unnecessarily.

**Bug 2 — `sell = False` initialization:** `not sell` was always True at the start, making the first branch always execute regardless of whether a stock was actually held.

**Bug 3 — Root cause (conceptual):** The constraint "at most one stock held at a time" was being taken too literally. The implementation was trying to physically simulate every buy/sell action — tracking hold state, checking next day's price before deciding to sell, etc. This over-complication caused the logic to break on several edge cases.

---

## Key Observation (Derived During Session)

On `[7, 1, 5, 3, 6, 4]`:
- Buy at 7 — never sold (stranded)
- Buy at 1, sell at 5 — profit 4
- Buy at 3, sell at 6 — profit 3
- Buy at 4 — never sold (stranded)

Two stocks were "stranded" — bought but never sold. In real trading this violates the "one stock at a time" constraint. But for **maximum profit calculation**, stranded stocks have 0 net contribution (no loss, no gain). They don't affect the answer.

**This means:** Explicitly tracking the "one stock at a time" constraint is unnecessary for computing maximum profit. The mathematical effect (consecutive positive differences) captures everything. The constraint simulation adds complexity without changing the answer.

This is a core greedy insight — **sometimes simulating a constraint is not necessary; only its mathematical effect matters.**

---

## Attempt 2 — Simple Consecutive Difference, Accepted ✅

### Thinking

Dropped all state tracking. Just iterate through consecutive pairs — if today's price is higher than yesterday's, that difference is profit. Sum all such differences.

### Code (GFG)

```python
class Solution:
    def stockBuySell(self, arr):
        profit = 0
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                profit += arr[i] - arr[i-1]
        return profit
```

### LC 122 Code (same logic, different return)

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit
```

### Result — All TC passed on GFG ✅, Accepted on LC 122 ✅

---

## Why Greedy Works — Mathematical Equivalence

For any sequence of prices `[a, b, c, d]` where `a < b < c < d`:
- Buy at `a`, sell at `d` → profit = `d - a`
- Buy at `a`, sell at `b`, buy at `b`, sell at `c`, buy at `c`, sell at `d` → profit = `(b-a) + (c-b) + (d-c) = d - a`

Same result. Consecutive differences always sum to the total range — any longer hold is mathematically equivalent to collecting every small gain along the way. Dropping days gives 0 contribution, so they're safely ignored.

---

## Complexities

| | Time | Space |
|---|---|---|
| Attempt 1 | O(n) | O(1) |
| Attempt 2 | O(n) | O(1) |

**Note:** Both approaches are O(n) time — Attempt 2 is just far simpler and correct. No sorting needed here unlike most greedy problems this week — single pass is sufficient.