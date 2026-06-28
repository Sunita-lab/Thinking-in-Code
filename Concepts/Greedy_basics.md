# Greedy Algorithms — Core Concept

**Week:** 9 | Day 1  
**Topic:** What is Greedy, when it works, when it doesn't

---

## What is Greedy?

Greedy is a designed, deliberate strategy — not a blind search. Someone observes that in a particular problem, making the locally optimal choice at every step leads to a globally optimal result. They prove it, and that becomes the rule.

At every step, greedy picks what looks best right now — and never goes back. No backtracking. No reconsidering past decisions. Whatever choice was made, is made.

> "Jo abhi best dikh raha hai wo karo."

---

## Brute Force vs Greedy

**Brute force** — when no rule is visible, try every possible combination or path, calculate results, pick the best one. It considers everything — all attributes, all sequences, all possibilities. Correct, but slow.

**Greedy** — a smart rule is derived first. Then follow that rule step by step without looking back. No combinations, no exhaustive search. Fast, but only correct when the rule holds.

| | Brute Force | Greedy |
|---|---|---|
| Approach | Try all possibilities | Follow one derived rule |
| Backtracking | Yes | Never |
| Speed | Slow | Fast |
| Always correct | Yes | Only when greedy choice property holds |
| Design effort | Low | High — finding the right rule is hard |

---

## When Does Greedy Work?

Greedy works when making the locally optimal choice does not disturb future choices — that is, the current decision does not make the remaining problem worse.

This is called the **greedy choice property** — a locally optimal choice can be part of a globally optimal solution.

**Auto-rickshaw example (derived in session):**  
Trips available with different earnings and time durations. Greedy by highest earnings failed — it picked a long trip that blocked two smaller trips worth more combined.

The correct greedy rule was **earliest finish time first** — not because it maximizes immediate earnings, but because it leaves maximum time available for future trips. The attribute that mattered was not money, but how much future opportunity the current choice preserved.

This is the core insight — **the right attribute to be greedy on is the one whose locally optimal choice does not hurt the remaining problem.**

---

## When Does Greedy Fail?

Greedy fails when the locally best choice blocks a better global outcome.

**Classic example — Hill Climbing:**  
Hill climbing always moves to the best neighboring state. But it can get stuck at a local maximum — a point that looks best in its neighborhood but is not the global best. From there, every neighbor looks worse, so greedy stops. It never explored the path that would have led to the true peak.

**Coin Change (arbitrary denominations):**  
With coins `[1, 3, 4]` and target `6` — greedy (largest first) picks `4`, then two `1`s → 3 coins. But optimal is `3 + 3` → 2 coins. Greedy failed because the coin denominations are not multiples of each other — one choice hurt the remaining subproblem.

**Key signal:** If multiple attributes interact with each other and one choice affects how well remaining choices can be made — pure greedy on one attribute is likely to fail.

---

## Greedy vs Dynamic Programming

Both build solutions step by step. The difference is in how decisions are made.

- **Greedy** makes a locally optimal choice at each step and never looks back. One pass, no memory of past subproblems.
- **DP** considers all past subproblems before making a choice. Looks everywhere back, not just one step.

A common interview trap — a problem looks greedy but requires DP, or vice versa. The distinction comes from whether the greedy choice property actually holds for that problem.

---

## Deriving the Right Greedy Rule

The hard part of greedy is not coding — it is finding the right attribute to be greedy on.

Steps:
1. Identify what you are optimizing (maximize count, minimize cost, etc.)
2. Think about what attribute, if chosen optimally at each step, does not hurt future steps
3. Verify — does a locally optimal choice on this attribute always lead to a globally optimal result?
4. If yes — that is your greedy rule. Sort or prioritize by that attribute and iterate.

---

## Summary

- Greedy is a deliberate, derived strategy — not guesswork
- It picks the locally optimal choice at every step, never backtracks
- It works only when the greedy choice property holds — local optimal does not block global optimal
- The right attribute to be greedy on must be identified and justified, not assumed
- Greedy is faster than brute force but requires proof of correctness
- When greedy fails — DP is usually the answer