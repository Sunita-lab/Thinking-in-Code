# DP as a DAG of States

**First articulated:** Week 17, Day 2 — after deriving 0/1 Knapsack's recurrence, while discussing why circular dependencies break standard DP.

---

## The core mental model

DP is fundamentally about organizing subproblems as a **DAG (Directed Acyclic Graph)**:

- **Node = a "state"** — a specific combination of parameters that fully defines one subproblem. E.g., in 0/1 Knapsack, a state is `(item_index, remaining_capacity)` — two numbers together uniquely describe one subproblem ("best value achievable from item_index onward, given remaining_capacity"). In Day 1's Fibonacci, a state was just a single number `n`.
- **Edge = a dependency** — a **directed** connection from state A to state B meaning "A's answer requires B's answer." Direction matters: it's A→B (A needs B), never a two-way relationship.
- **Acyclic** — following dependencies from any state can never lead back to that same state. This is what guarantees a valid "bottom" exists (a base case) and that there's *some* order in which every state's dependencies get resolved before the state itself is computed.

## What DP is actually doing under the hood

DP explores the same set of subproblems that brute force would — it isn't magic that skips work. What it changes is: **every unique state (node in the DAG) gets solved exactly once**, and its result gets stored and reused wherever that same state is needed again, instead of being recomputed. This is the same idea already captured in `dp_vs_greedy_core_distinction.md` — DP avoids *recurring* computation, not computation itself — restated here in graph terms: the DAG structure is *why* recurring computation is avoidable — the same node can have multiple incoming edges (multiple other states depend on it), and it only needs to be resolved once regardless of how many places point to it.

## Why acyclicity is required

If the dependency graph had a cycle (state A needs state B, which needs state A), there would be no valid "starting point" — no state could be fully resolved without first resolving another state that itself isn't resolvable without the first. There's no base case to bottom out at. Standard memoization/tabulation has no way to handle this, because both techniques fundamentally rely on: process states in an order where each state's dependencies are already done.

**Real DP problems are always DAGs even when they don't look like one at first** — e.g., a problem needing "best value from the left" and "best value from the right" at every position isn't circular, because it decomposes into two independent one-directional passes (see the addendum in `week17/concepts/concept_0_1_knapsack.md` for the worked-through distinction). True cycles (e.g., some expected-value/probability recurrences where a state depends on another state that depends back on it) fall outside what ordinary DP can solve and need different tools (simultaneous equations, iterative convergence).

## Practical use of this model

When starting a new DP problem, it helps to explicitly ask:
1. **What is "a state" here?** (What minimal set of parameters fully describes one subproblem? This was the hard part in 0/1 Knapsack — realizing "value so far" was *not* part of the state, only `(index, remaining_capacity)` was.)
2. **What does each state depend on?** (This gives the recurrence.)
3. **Is the dependency graph acyclic?** (If yes, proceed with normal memoization/tabulation. If a genuine cycle appears, DP in its standard form won't work — look for a different technique.)
4. **What's the base case?** (The node(s) with no outgoing edges — the natural "bottom" of the DAG.)

## Where this will recur

Every DP problem going forward benefits from this framing — it's the general lens for "what is the state, what does it depend on, is there a valid processing order." Multi-dimensional states (2D, 3D tables) are just states with more parameters — the DAG idea doesn't change, only the number of coordinates needed to name a node.

---

## Addendum — Base cases aren't always at a "corner"; topological order isn't always a simple sweep

**First raised:** Week 17, Day 6 — while solving Triangular Path Sum, asking whether a base case could ever sit in the "middle" of a table, and whether traversal would need to go in many directions from there.

### Can a base case ever be a "middle" cell, with dependencies radiating outward in many directions?

Not in the sense of being arbitrary or lacking any special structure — a base case is always the state (or one of several states) that is **simplest/smallest** with respect to *some* parameter, even if that parameter isn't the raw row/column index a 2D table visually suggests.

**A concrete illustration (from Interval DP, a later topic — e.g. Longest Palindromic Subsequence, Matrix Chain Multiplication):** state is often `dp[i][j]` representing an interval `[i,j]`. The base case is `i == j` (a length-1 interval) — but plotted on a 2D grid, `i==j` is the **diagonal**, which looks visually like it's "in the middle" of the table, not a corner or edge. It isn't actually a complex, many-directions base case though — it's still the simplest possible state, just measured by **interval length**, not by row/column position. The fix is to iterate by **length** (`length = 1, 2, 3, ...`) rather than by row or column directly — this automatically visits every state in a valid dependency order, without needing to think about "which direction to sweep."

### What if dependencies genuinely radiate outward in many directions (e.g. 8 directions from a central cell)?

This can happen in some specialized problems (e.g. wave-propagation-style states). The resolution is the same idea generalized: DP doesn't require iterating by literal row/column direction — it requires finding **some monotonic parameter** that measures "distance/layers from the base case" (e.g. Manhattan distance, BFS-layer number), and processing states in increasing order of that parameter. This guarantees that whenever a state is processed, everything it depends on (always at a strictly smaller "distance") has already been resolved — a **topological order**, just not necessarily a simple linear sweep across rows or columns.

**Connects directly to the core DAG model above:** a DAG's topological order doesn't have to look like "top-to-bottom, left-to-right." Any ordering that respects "dependencies come before dependents" is valid — sometimes that's a simple 2D sweep, sometimes it's ordering by interval length, sometimes it's ordering by distance-from-source. If no such monotonic/topological ordering can be found at all, that's exactly the earlier-established signal that the dependency graph has a genuine cycle, and standard DP won't work (see the main "genuinely circular dependency" discussion above).