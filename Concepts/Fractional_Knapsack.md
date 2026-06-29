# Fractional Knapsack — Concept Notes

**Week:** 9 | Day 2  
**Topic:** Fractional Knapsack — What it is, why greedy works, why 0/1 doesn't

---

## What is Fractional Knapsack?

A jar has a fixed capacity. There are items, each with a weight and a value. The goal is to maximize the total value in the jar without exceeding its capacity. Fractions of items are allowed — you can take a part of an item.

---

## Naive Approaches (and why they fail)

Before arriving at the correct greedy rule, two naive strategies were considered:

**Strategy 1 — Smallest weight first:**  
Intuition — take as many items as possible by picking the lightest ones first.  
Problem — a very light item might have very low value. Filling the jar with low-value items wastes capacity that could have held something more valuable.

**Strategy 2 — Highest value first:**  
Intuition — grab the most valuable items first.  
Problem — a very valuable item might be very heavy. It consumes too much capacity, leaving little room for other items that could collectively add more value.

Both strategies fail because they look at only one attribute — either weight or value — while ignoring how the two interact.

---

## The Correct Greedy Rule — Value/Weight Ratio

When two attributes interact, greedy on either one alone fails. The solution is to combine them into a single attribute that captures both — the **value/weight ratio**.

Ratio = value / weight — how much value you get per unit of weight.

**Greedy rule:** Sort items by ratio in descending order. Pick the highest ratio item first. If it fits completely, take it whole. If it does not fit, take as much of it as possible (fraction allowed).

This works because taking the highest ratio item never hurts future choices — fraction allowed means remaining capacity is never wasted. Whatever space is left, the next best ratio item fills it.

---

## Why Fraction Allowed Makes Greedy Safe

If fractions were not allowed (0/1 Knapsack), greedy would fail. A heavy item with the best ratio could consume most of the capacity, leaving a gap that no remaining whole item fits into. Meanwhile, a combination of lighter items could have filled the jar with more total value.

Fraction allowed eliminates this problem — remaining capacity is always fillable. The jar will always be packed optimally. This is what makes greedy correct here.

---

## Why 0/1 Knapsack Needs DP

In 0/1 Knapsack, each item is either taken whole or not taken. Greedy fails because one heavy high-ratio item can block better combinations.

DP solves this by exploring both choices for every item — take it or leave it — and storing results of subproblems to avoid recomputation. It considers all possibilities efficiently, which greedy never does.

| | Greedy | DP |
|---|---|---|
| Explores possibilities | No — one rule, one pass | Yes — all choices per item |
| Backtracks | Never | Not exactly, but stores all subproblem results |
| Works for Fractional | Yes | Yes (overkill) |
| Works for 0/1 | No | Yes |

---

## Connection to Core Greedy Principle

This problem is a direct application of what was derived on Day 1 — greedy works when the locally optimal choice does not hurt future choices. Here, the ratio captures both attributes together, and fraction allowed ensures remaining capacity is never wasted. Both conditions hold — greedy is safe.

---

## Summary

- Fractional Knapsack — maximize value in a capacity-constrained jar, fractions allowed
- Naive approaches (smallest weight first, highest value first) both fail — single attribute greedy is not enough
- Correct rule — sort by value/weight ratio descending, take greedily
- Fraction allowed is what makes greedy correct — remaining capacity never goes to waste
- 0/1 Knapsack (no fractions) — greedy fails, DP needed