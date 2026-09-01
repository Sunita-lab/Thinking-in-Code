# Chocolates Pickup (GFG) / Cherry Pickup II (LC 1463)

**Day:** Week 17, Day 6 — Matrix/Triangle Path (bonus, most complex problem of the week)
**Status:** Solved after a substantial debugging and conceptual-clarification journey — the most involved problem of Week 17

---

## Problem Statement

An `m x n` grid of chocolate counts. Two robots move simultaneously, row by row, from row 0 to the last row. Robot 1 starts at `(0,0)`, Robot 2 starts at `(0, cols-1)`. Each row, each robot independently moves to one of three columns in the next row: `c-1`, `c`, or `c+1`. Maximize total chocolates collected; if both robots are ever on the same cell, that cell's chocolate is counted only once.

---

## The Derivation Journey

### Step 1 — Identifying the state

Correctly identified the state needs **three** parameters: `(row, robot1_col, robot2_col)` — reasoning that both robots are always on the same row simultaneously (since they move together), so only the row and each robot's column need tracking. This is a **3D state**, requiring a 3D table, directly extending the "count the independent parameters" principle from `general_concepts/dp_problem_solving_workflow.md`.

### Step 2 — Recurrence, built up over several corrections

**First raw attempt** multiplied two separately-maxed sub-results (`max(robot1 options) * max(robot2 options)`) — corrected after recognizing the state is a single combined `(row, c1, c2)` triple, not two independent states, so all **9** combinations of (Robot1's 3 choices × Robot2's 3 choices) needed to be enumerated and maxed together, not combined via two separate `max()` calls multiplied together. All 9 `(c1±{-1,0,1}, c2±{-1,0,1})` pairs were correctly enumerated once this was pointed out.

**Double-counting rule:** correctly built into the recurrence — `grid[r][c1] + grid[r][c2]` when `c1 != c2`, but just `grid[r][c1]` when `c1 == c2`.

---

## Bug 1 — Base case only partially initialized

### Buggy attempt
```python
dp[0][0][0] = grid[0][0]
dp[0][cols-1][0] = grid[0][cols-1]
```
Only two specific cells were set, leaving the rest of row 0 at their default `0`.

**Bug found via testing (bash):** crashed with an `IndexError`, and — more importantly — even before the crash, the underlying logic was wrong. The recurrence for row 1 references `dp[0][j1-1][j2]`, `dp[0][j1][j2+1]`, etc. — essentially **arbitrary** `(c1,c2)` combinations from row 0, not just the two manually-set cells. Fixed by filling **all** `(c1,c2)` combinations in the base-case row via a full double loop.

**Root cause:** conflating "we only care about ONE specific cell as the final answer" with "we only need to initialize that one cell." These are different things — see the major conceptual discussion below.

---

## Bug 2 — Directional confusion: forward vs backward DP

### The core mistake

Initially treated **row 0** as the base case (direct values, no dependency) and built **forward** (`dp[i]` computed from `dp[i-1]`), then read the final answer from `dp[0][0][cols-1]` — but row 0 was *also* being used as both the base case AND the answer source, meaning the middle/later rows were never actually used in computing the returned value. This was caught by manually tracing a tiny 2-row example and noticing the returned `dp[0][...]` value didn't reflect any real path through the whole grid.

### The resolution — figuring out which direction is correct

Worked through by contrasting this problem against Max Path Sum in Matrix (solved earlier the same day):

| Problem | Start | End | Formulation | Base case row | Loop direction | Final answer |
|---|---|---|---|---|---|---|
| **Max Path Sum in Matrix / Triangle** | Free (Matrix) or trivially-unique (Triangle: only 1 cell in row 0) | Free (any column in last row) | Prefix (`dp[r]="best sum arriving here"`) | Row 0, all combinations | Forward (`dp[r-1]→dp[r]`) | `max/min(dp[last_row])` |
| **Chocolates Pickup** | Fixed (only `(0, cols-1)` is valid) | Free (any `(c1,c2)` in last row) | Suffix (`dp[r]="best from here onward"`) | Last row, all combinations | Backward (`dp[r+1]→dp[r]`) | `dp[0][0][cols-1]` |

**The precise reasoning (refined after further discussion — see full derivation in `general_concepts/dp_free_vs_fixed_endpoint.md`):**

Two different questions can be asked of any state, and they behave differently:
- **Prefix question:** "what's the best total value of a path that genuinely started at the true start and has arrived here?" — this requires knowing whether the state is actually **reachable** from the true start. At row 0, only `(0,cols-1)` is reachable (no moves have happened yet); every other `(c1,c2)` combination is a fictional, impossible configuration at that point.
- **Suffix question:** "if I were at this state, what's the best I could do from here onward?" — this is **always** well-defined for any state, whether or not it's actually reachable from the true start.

**Empirically verified both formulations work when done correctly:** re-implemented using the Prefix/forward approach, but this time explicitly marking every row-0 combination *except* `(0,cols-1)` as `-infinity` (invalid, unreachable) rather than giving them real values — tested against the working Suffix/backward solution across 3 cases, **identical results**. This confirmed that a fixed endpoint *can* be a valid base case — the original bug wasn't "fixed endpoints can never be base cases," it was **failing to mark invalid states as invalid**, silently treating every row-0 combination as equally legitimate when only one actually was.

**Why Suffix/backward was still the cleaner choice here:** it completely avoids the need for any validity/reachability marking — "best from here onward" doesn't care how you got to a state, so every cell in the base-case (last) row is automatically meaningful with no extra bookkeeping. Prefix/forward would have worked too, but only by remembering to explicitly invalidate every non-start combination at row 0 — an easy step to forget (as the original bug demonstrated).

**Why Max Path Sum in Matrix could safely use row 0 as-is (no invalidation needed):** its problem statement explicitly allows starting from *any* column — so every combination at row 0 genuinely is a valid starting configuration, no fictional states exist there to worry about. The "nature of the problem" difference is precisely this: whether the starting configuration is stated as free/arbitrary (Max Path Sum) or pinned to one specific given configuration (Chocolates Pickup).

**Comparison with Triangle (same day):** Triangle also used Prefix/forward DP (base case at row 0), which seemed to contradict the "fixed start is problematic" idea at first glance — resolved by noting Triangle's row 0 has only **one cell** (`(0,0)`) to begin with. "Start is free" and "start is fixed to the only option that exists" collapse into the same situation when there's no other (even fictional) combination sharing that row to accidentally mark as valid.

### Concrete example illustrating "starting condition ≠ base case"

Even after understanding *which* row is the base case, a further point of confusion was clarified with a fully worked 2×2 example (`grid=[[1,2],[3,4]]`):

`dp[0][0][1]` (row 0, robot1 at col 0, robot2 at col 1 — the actual known start) is **not itself a base case** — computing it still requires looking at the *entire rest of the grid* (row 1's four possible `(c1,c2)` states and taking the best). It only differs from any other `dp[0][c1][c2]` in that we happen to *know in advance* which cell holds the final answer — it does **not** mean that cell's computation skips the recursive "look at the future" step. The true base case is `dp[last_row][*][*]`, where recursion genuinely terminates (no further row to look ahead to).

**General statement of this insight:** knowing which cell in the table will hold the final answer (because the problem tells you the starting configuration) is a completely separate fact from that cell being a base case. A base case is defined by having **no further dependency** — an answer being "at a known location" says nothing about whether computing it requires further recursion or not.

---

## Bug 3 — Missing `self` parameter in helper method

### Buggy attempt
```python
def idx(rows,cols,x,y1,y2,dp):
    ...
```
Called as `self.idx(rows,cols,i+1,j1-1,j2,dp)` — since `self.method(...)` implicitly passes `self` as the first positional argument, and the function signature's first parameter was `rows` (not `self`), all arguments shifted by one position. **Bug found via testing (bash):** `TypeError: idx() takes 6 positional arguments but 7 were given`.

**Fix:** `def idx(self, rows, cols, x, y1, y2, dp):`

---

## Bug 4 — Silent negative-index wraparound (caught before it caused a wrong answer)

Before writing the `idx()` helper, boundary checks were done with raw indexing (`dp[i+1][j1-1][j2]`), which for `j1=0` accesses `dp[i+1][-1][j2]`. **Demonstrated via a small Python example** that this does **not** raise an error — Python interprets negative indices by wrapping around to count from the end of the list (`a[-1]` = last element), silently returning a **completely unrelated, wrong** value instead of crashing.

This is a more dangerous class of bug than an `IndexError`, because it doesn't announce itself — the code runs and produces a plausible-looking (but wrong) number. The `idx()` helper function was introduced specifically to guard against this: explicitly checking `0 <= x < rows` and `0 <= y1,y2 < cols` before indexing, returning `float('-inf')` for any invalid combination so `max()` naturally never selects it.

---

## Final Code

```python
class Solution:
    def idx(self, rows, cols, x, y1, y2, dp):
        if x >= 0 and x < rows and y1 >= 0 and y1 < cols and y2 >= 0 and y2 < cols:
            return dp[x][y1][y2]
        else:
            return float('-inf')

    def maxChocolate(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        dp = [[[0 for _ in range(cols)] for _ in range(cols)] for _ in range(rows)]
        for j1 in range(0, cols):
            for j2 in range(0, cols):
                dp[rows-1][j1][j2] = grid[rows-1][j1]+grid[rows-1][j2] if j1 != j2 else grid[rows-1][j1]
        for i in range(rows-2, -1, -1):
            for j1 in range(0, cols):
                for j2 in range(cols-1, -1, -1):
                    if j1 != j2:
                        dp[i][j1][j2] = grid[i][j1] + grid[i][j2] + max(
                            dp[i+1][j1][j2],
                            self.idx(rows,cols,i+1,j1-1,j2,dp), self.idx(rows,cols,i+1,j1+1,j2,dp),
                            self.idx(rows,cols,i+1,j1,j2-1,dp), self.idx(rows,cols,i+1,j1,j2+1,dp),
                            self.idx(rows,cols,i+1,j1-1,j2+1,dp), self.idx(rows,cols,i+1,j1+1,j2-1,dp),
                            self.idx(rows,cols,i+1,j1+1,j2+1,dp), self.idx(rows,cols,i+1,j1-1,j2-1,dp))
                    else:
                        dp[i][j1][j2] = grid[i][j1] + max(
                            dp[i+1][j1][j2],
                            self.idx(rows,cols,i+1,j1-1,j2,dp), self.idx(rows,cols,i+1,j1+1,j2,dp),
                            self.idx(rows,cols,i+1,j1,j2-1,dp), self.idx(rows,cols,i+1,j1,j2+1,dp),
                            self.idx(rows,cols,i+1,j1-1,j2+1,dp), self.idx(rows,cols,i+1,j1+1,j2-1,dp),
                            self.idx(rows,cols,i+1,j1+1,j2+1,dp), self.idx(rows,cols,i+1,j1-1,j2-1,dp))
        return dp[0][0][cols-1]
```

Verified via bash against a memoized-recursion reference across 5 test cases (including a single-row grid) — all matched.

---

## Complexity

- **Time:** O(rows × cols²) — for each row, iterating over all `(c1,c2)` pairs (`cols²`) and checking up to 9 neighbors each
- **Space:** O(rows × cols²)

---

## Mid-way Doubts

### Whether `j2`'s loop direction (reverse vs forward) matters
Raised directly, with the instinct that it should matter (carried over from earlier problems where loop direction was critical) but a competing intuition — trusting the DAG-of-states model — suggesting it might not. **Tested empirically (bash):** running `j2` in reverse vs forward order produced **identical** results. Confirmed why: `dp[i][j1][j2]` only ever depends on `dp[i+1][...]` (a completely different, already-fully-computed row) — never on another cell in the *same* row `i`. Since there's no same-row dependency, the order of iterating within row `i` (for either `j1` or `j2`) is irrelevant — this is the same "no same-row dependency → order doesn't matter" reasoning already established in `general_concepts/dp_trust_and_redundant_branches.md` for the Unbounded Knapsack column-order question.

### Attempted syntax: combining two loop ranges into one `for` statement
Tried `for j1 in range(0,cols) and j2 in range(cols-1,-1,-1):` expecting it to iterate both simultaneously — this is not valid Python; `and` doesn't combine iterables in a `for` statement. Two independent ranges that both need to vary (a full cross-product of combinations) require either nested loops (as ultimately used) or `itertools.product()` for a single flattened loop — noted for future reference, not used here.

## Syntax / Python Concepts Touched

- Instance methods require `self` as the explicit first parameter in their definition — omitting it causes `self.method(...)` calls to silently shift every other argument by one position, producing a `TypeError` about argument count rather than a clear "missing self" message.
- Negative list indices in Python wrap around to count from the end (`a[-1]` = last element) rather than raising an error — this makes forgetting a boundary check a **silent** bug (wrong value, no crash) specifically on the *lower* boundary, whereas exceeding the *upper* boundary correctly raises `IndexError`. Both boundary directions need explicit guarding; they fail differently.
- `for x in range(a) and y in range(b):` is not valid syntax for a combined/nested loop in Python.

## Key Insight / Learning (Sunita's own words)

"Starting condition aur base condition dono ek baat nahi hoti. Ye baat mere liye jhatka dene wali hai."

**Elaborated with the concrete example:** knowing that the answer will ultimately be read from `dp[0][0][cols-1]` (because that's where the robots are known to start) does **not** mean that cell is a base case. Computing `dp[0][0][cols-1]` still requires the full recursive "look at every possible future" computation — it depends on `dp[1][...]`, which depends on `dp[2][...]`, all the way down to the genuine base case (the last row, where there truly is no further row to consider). A base case is defined purely by **having no further dependency to resolve** — not by being "the cell we care about" or "the cell corresponding to the problem's stated starting position." These are two independent facts about a DP table that can easily get conflated, especially in problems (like this one) where the starting configuration is a specific, non-trivial state rather than trivially unique (contrast with Triangle, where the fixed start also happened to be the *only* cell in its row, hiding this distinction).

This insight generalizes into the broader "free end vs fixed end" principle (fully worked out via the Max Path Sum in Matrix vs Triangle vs Chocolate Pickup comparison) — captured in `general_concepts/dp_free_vs_fixed_endpoint.md`.

## Aage ke liye Learning

- Before choosing which end of a path-DP problem to treat as the base case, explicitly check: at this end, is *every* possible state in the table genuinely valid (a legitimate starting/ending configuration), or only one specific state? Base cases belong at the end where all states are valid; specific known states (fixed by the problem, but not "free") are read as a single answer cell, not treated as a base case.
- "We only need the answer from one specific cell" and "that cell requires no further computation" are different claims — the first is about what the caller ultimately wants; the second is about whether recursion terminates there. Don't let knowing the answer's location convince you that cell is trivially computable.
- When writing an instance method (`def foo(self, ...)`), always double-check `self` is the first parameter — a missing `self` produces a somewhat confusing `TypeError` about argument counts rather than a direct "you forgot self" message.
- Negative Python indices don't crash — they silently wrap around. Any DP boundary-checking logic must explicitly guard against indices going negative, not just against exceeding the upper bound (which does crash and is comparatively safer to accidentally catch).