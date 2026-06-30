# Activity Selection — Concept Notes

**Week:** 9 | Day 3  
**Topic:** Activity Selection — count maximization, connection to greedy choice property and the fraction-allowed insight

---

## What is Activity Selection?

Given a set of activities, each with a start time and finish time, select the maximum number of activities that can be performed by a single person, assuming a person can only work on one activity at a time (no overlaps allowed).

The goal is purely to **maximize count** — there is no value or weight attached to individual activities.

---

## Naive Approach

Generate all possible subsets of activities, check which ones are non-overlapping, and pick the subset with the maximum size. This takes exponential time — far too slow for practical input sizes.

---

## Greedy Strategy — Earliest Finish Time First

Sort activities by finish time. Pick the activity that finishes earliest. Then, among remaining activities, pick the next one whose start time is greater than the previous activity's finish time. Repeat.

**Why finish time and not start time or duration:** An activity that finishes early leaves the maximum possible time available for future activities. This preserves the most future opportunity — which is exactly the attribute that needs to be greedy-optimized when the goal is to maximize count.

---

## Connection to Day 1 — Auto-Rickshaw Example

Initially this looked structurally different from the Day 1 auto-rickshaw example, because the rickshaw problem also involved maximizing money (a value), not just count. This raised a doubt — are these really the same kind of problem?

On closer inspection: in the rickshaw example, earliest finish time also turned out to be the correct strategy — but only because count happened to align with value in that specific scenario. The deeper test was — does earliest-finish-time greedy hold when value/money is explicitly the objective, not just count?

**Counter-example constructed during the session:**

| Trip | Money | Time |
|------|-------|------|
| A | ₹100 | 9am–10am (finishes early) |
| B | ₹1000 | 9am–5pm (finishes late) |

If "earliest finish time" is followed blindly here (with money as the actual goal), Trip A gets picked first, blocking Trip B — total ₹100, when ₹1000 was available by skipping A.

**Conclusion:** "Earliest finish time" is guaranteed optimal only when the goal is to **maximize count** of non-overlapping activities. The moment a second attribute (value/money) enters the objective, pure greedy on finish time breaks down.

---

## Why Greedy Works for Pure Activity Selection but Not When Value Is Added

This connects directly back to the Fractional Knapsack insight from Day 2.

**Activity Selection (count only):** Only one attribute matters — time. The greedy choice (earliest finish) never reduces future opportunity, so the greedy choice property holds cleanly.

**Weighted Activity Selection (count + value):** Two attributes now interact — time and value. This is structurally similar to 0/1 Knapsack, not Fractional Knapsack, because:
- An activity is either selected entirely or not at all — there's no way to take a "fraction" of an activity's time slot to make it fit.
- Since fractions aren't allowed, one greedy choice can block a better combination of other activities, exactly like 0/1 Knapsack.

**Pattern derived during the session:**

| Attributes | Fraction Allowed? | Approach |
|---|---|---|
| 1 attribute | N/A | Greedy |
| 2 attributes | Yes (can partially take items) | Greedy (ratio-based, like Fractional Knapsack) |
| 2 attributes | No (all-or-nothing) | DP (like 0/1 Knapsack, Weighted Activity Selection) |

This is the same boundary discussed on Day 2 — fractional allowance is what keeps remaining capacity (or remaining time) always usable, which is what preserves the greedy choice property. Without it, a single choice can create an unusable gap that blocks a better combination — and only DP, which explores all combinations, can guarantee optimality.

---

## Tie-Breaking Rule

If two activities finish at the exact same time the activity that finished is considered done at that moment — a new activity starting at that same time is allowed (non-overlapping), since the convention treats end-time and start-time equality as non-conflicting (e.g., a slot ending at 9am and another starting at 9am don't overlap).

This is why the comparison condition uses strict `>` (next activity's start time must be strictly greater than current finish time) — not `>=` — when checking if back-to-back activities at the same boundary point are valid.

---

## Summary

- Activity Selection maximizes count of non-overlapping activities — a single-attribute greedy problem
- Greedy rule — sort by finish time, pick earliest finish, then next activity whose start > previous finish
- The auto-rickshaw analogy from Day 1 only holds when the objective is pure count, not value
- The moment value enters the picture and fractions aren't allowed, the problem becomes 0/1 Knapsack-like and needs DP
- This reconnects with the Day 2 insight: fraction-allowed → greedy works (ratio-based); fraction-not-allowed + multiple attributes → DP needed