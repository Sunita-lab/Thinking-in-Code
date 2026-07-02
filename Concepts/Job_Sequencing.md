# Job Sequencing — Concept Notes

**Week:** 9 | Day 4  
**Topic:** Job Sequencing — profit maximization with deadlines, greedy rule derivation

---

## What is Job Sequencing?

Given a list of jobs, each with a deadline and a profit, and knowing that each job takes exactly 1 unit of time to complete — select a subset of jobs to maximize total profit. A job can only be done if it is completed on or before its deadline.

---

## Naive Approach

Generate all possible subsets of jobs, check which subsets are schedulable within deadlines, and pick the one with maximum profit. Exponential time — not practical.

---

## Greedy Strategy — Highest Profit First, Latest Available Slot

**Step 1 — Sort by profit descending:** The most valuable jobs should be considered first. If two jobs compete for the same slot, the higher profit job should win.

**Step 2 — For each job, assign the latest available slot within its deadline:** If a job has deadline 3, it can go in slot 1, 2, or 3. The latest available slot should be preferred — this keeps earlier slots free for jobs with smaller deadlines that have fewer options.

**Why latest slot, not earliest?** A job with deadline 1 can only go in slot 1. A job with deadline 3 can go in slot 1, 2, or 3. If the deadline-3 job takes slot 1, the deadline-1 job has nowhere to go. By always picking the latest available slot, we preserve earlier slots for more constrained jobs — maximizing the number of schedulable jobs and thus profit.

---

## Why Greedy Works Here

The greedy choice property holds — taking the highest profit available job and assigning it to its latest available slot never prevents a better solution. Any other assignment (taking a lower profit job first, or using an earlier slot unnecessarily) can only result in equal or worse total profit.

This is the same "preserve future opportunity" principle seen throughout Week 9 — the greedy choice is the one that keeps the most options open for future decisions.

---

## Slot Tracking — Two Approaches

### Approach 1 — Boolean Array (O(n × maxDeadline))

Maintain a `slots[]` boolean array. For each job, scan backwards from its deadline to find the latest free slot. Simple to implement and understand, but slow for large deadline values.

### Approach 2 — Disjoint Set Union (O(n log n))

Use a DSU data structure where each slot points to the next available slot below it. `find(deadline)` instantly returns the latest available slot ≤ deadline without scanning. `merge` updates the pointer so future queries skip occupied slots automatically.

DSU is the optimal approach — but requires understanding of the Disjoint Set Union data structure, which is formally covered in Graph week. The greedy logic is identical in both approaches; DSU only changes how slot lookup is performed.

---

## Connection to Week 9 Greedy Theme

| Problem | Greedy Attribute | Why It Works |
|---|---|---|
| Activity Selection | Earliest finish time | Preserves maximum future time |
| Job Sequencing | Highest profit first + latest slot | Preserves earlier slots for constrained jobs |
| Fractional Knapsack | Highest value/weight ratio | Best return per unit of capacity |

All three follow the same meta-principle — the greedy choice is the one that maximizes future opportunity while making the best local decision.

---

## Summary

- Sort jobs by profit descending
- For each job, assign the latest available slot within its deadline
- If no slot available, skip the job
- Boolean array approach: correct but O(n × maxDeadline) — TLE on extreme inputs
- DSU approach: same greedy logic, O(n log n) — optimal, uses path compression for fast slot lookup
- DSU formally covered in Graph week — revisit this problem then for full understanding