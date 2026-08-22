# Problem: Count Islands (GFG) — 8-directional (diagonals included)

**Week 16 — Day 5 — Grid Graphs (Traversal Applications)**

**Similar to LC 200 (Number of Islands) — but LC 200 typically uses only 4-directional adjacency; this GFG version explicitly allows diagonal connections (8-directional). Different enough that they're treated as related-but-distinct here.**

## Problem Statement
Grid diya hai (`'L'` = land, `'W'` = water). Count total islands — ek island = connected land cells ka group, jahan connections **8-directional** hain (horizontal, vertical, AND diagonal).

## Concept Connection
Grid ke cells = nodes. Connections = edges (implicit, based on adjacency in the grid, not explicitly listed). "Island counting" = "connected components counting" applied to a grid — same core DFS/BFS idea as Day 4's connected components concept, just on an implicit grid-graph instead of an explicit edge-list graph.

## My Approach — iterative construction, many small bugs (documented as a full build-up journey)

### Step 1: Direction offsets (8 directions)
```python
direc = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1,1), (1, -1)]
```
Ek baar define kiya, reusable for any cell — row/col offsets for all 8 neighbor directions.

### Step 2: `findneighbors` helper — get valid (in-bounds) neighbors of a cell
```python
def findneighbors(self, row, col, direc, n):
    neigh = []
    for d in direc:
        row_new = row + d[0]
        col_new = col + d[1]
        if row_new >= 0 and row_new < n and col_new >= 0 and col_new < n:
            neigh.append((row_new, col_new))
    return neigh
```
Initial version assumed **square grid** (single `n` for both row and column bounds) — later found to be a bug for rectangular grids.

### Step 3-6: `search` (recursive DFS) — multiple bugs found and fixed one at a time

**Bug A — forgot `self` in method signature** (first draft had `def findneighbors(row, col, direc, n):` without `self`) — fixed by adding `self` as first param, since it's a class method.

**Bug B — single-level neighbor check, no recursion**: First `search` attempt only inspected immediate neighbors and marked them visited, without recursing further — meaning a long chain of connected land cells would only get the first layer marked, missing the rest. Fixed by making `search` call itself recursively on each newly-found land neighbor (same DFS pattern as Day 3).

**Bug C — checking grid VALUE against `visited` set instead of POSITION**:
```python
only_L = [x for x in surr if grid[x[0]][x[1]] == 'L' and grid[x[0]][x[1]] not in visited]
```
This checked `grid[x[0]][x[1]] not in visited` — i.e., checking if the **character `'L'`** is in the visited set, which is meaningless (visited should store *positions*, not grid values). This bug appeared in **two places** — inside `search`'s list comprehension, AND in `countIslands`'s main loop (`grid[i][j] not in visited`). Fixed by changing both to check `(x[0], x[1]) not in visited` / `(i,j) not in visited` — checking the **position tuple**, not the cell's content.

**Bug D — missing arguments in recursive call**: `self.search(l[0], l[1], visited, grid, surr)` was missing `direc` and `n` (function signature required 7 args after `self`, only 5 were passed) — Python would raise a `TypeError` for missing positional arguments. Fixed by passing all required args consistently.

**Bug E — square-grid assumption breaking on rectangular grids**: `findneighbors` used a single `n` to bound-check both row and column (`row_new < n and col_new < n`). On a rectangular grid (rows ≠ columns), this either wrongly rejected valid columns or wrongly accepted out-of-range columns — leading to an `IndexError`/runtime error when accessing `grid[row][out_of_range_col]`. Fixed by introducing a separate `m` (column count, `len(grid[0])`) alongside `n` (row count, `len(grid)`), and using `row_new < n` and `col_new < m` separately.

### Final Working Code
```python
class Solution:
    def findneighbors(self, row, col, direc, n, m):
        neigh = []
        for d in direc:
            row_new = row + d[0]
            col_new = col + d[1]
            if row_new >= 0 and row_new < n and col_new >= 0 and col_new < m:
                neigh.append((row_new, col_new))
        return neigh

    def search(self, i, j, visited, grid, surr, direc, n, m):
        visited.add((i,j))
        only_L = [x for x in surr if grid[x[0]][x[1]] == 'L' and (x[0], x[1]) not in visited]
        for l in only_L:
            surr = self.findneighbors(l[0], l[1], direc, n, m)
            self.search(l[0], l[1], visited, grid, surr, direc, n, m)

    def countIslands(self, grid):
        direc = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1,1), (1, -1)]
        n = len(grid)
        m = len(grid[0])
        visited = set()
        islands = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'L' and (i,j) not in visited:
                    islands += 1
                    surr = self.findneighbors(i, j, direc, n, m)
                    self.search(i, j, visited, grid, surr, direc, n, m)
        return islands
```
**Accepted.**

## Concrete Trace — verifying the diagonal-connectivity logic
Input:
```
L L W
W L W
W W L
```
Expected: **1 island** (all land cells connect via a chain including a diagonal step from (1,1) to (2,2)).

```
i=0,j=0: grid[0][0]='L', (0,0) not in visited -> islands=1
  search(0,0,...): visited={(0,0)}
    neighbors of (0,0) [bounded]: (0,1),(1,0),(1,1)
    only_L (land AND unvisited): (0,1) is 'L' -> yes. (1,0) is 'W' -> no. (1,1) is 'L' -> yes.
    only_L = [(0,1),(1,1)]

    recurse search(0,1,...): visited={(0,0),(0,1)}
      neighbors of (0,1): (0,0),(0,2),(1,0),(1,1),(1,2)
      only_L: (0,0) visited-skip. (0,2)='W'-skip. (1,0)='W'-skip. (1,1)='L', unvisited -> yes. (1,2)='W'-skip.
      only_L=[(1,1)]
      recurse search(1,1,...): visited={(0,0),(0,1),(1,1)}
        neighbors of (1,1): all 8 valid: (0,0),(0,1),(0,2),(1,0),(1,2),(2,0),(2,1),(2,2)
        only_L: (2,2)='L', unvisited -> yes (this is the DIAGONAL connection!)
        only_L=[(2,2)]
        recurse search(2,2,...): visited={(0,0),(0,1),(1,1),(2,2)}
          neighbors of (2,2): (1,1),(1,2),(2,1) [others out of bounds]
          only_L: (1,1) visited-skip. rest are 'W'.
          only_L=[] -> recursion ends here

    back in search(0,1,...): recurse search(1,1,...) already done via above chain (visited check prevents reprocessing)

  back in search(0,0,...): recurse search(1,1,...) — but (1,1) already visited, so only_L filtering would exclude it if reached again

Continue outer loop: all other 'L' cells ((0,1),(1,1),(2,2)) are already in visited, so no new islands counted.

Final: islands = 1  ✓ CORRECT
```

## (1) Mid-way doubts
- **Confusion at the start about "how to even approach this"** — grid-based DFS felt unfamiliar initially compared to explicit adjacency-list graphs from Days 1-4. Breaking it into sub-steps (direction offsets → neighbor-finder → recursive search → main loop) helped structure the confusion into solvable pieces.
- **`self` missing in method signature** — easy to forget when a helper method is added to an existing class.
- **Checking grid value against `visited` instead of position** — happened *twice* independently (once in `search`, once in `countIslands`'s main loop) — a recurring mental slip of "checking the wrong thing" (content vs. identity/position) that's worth watching for in future grid problems.
- **Square vs rectangular grid assumption** — didn't initially consider that `n` (rows) and `m` (columns) could differ; this is a common grid-problem trap.

## (2) Syntax / Python concepts touched
- List comprehension with tuple-unpacking-adjacent indexing (`x[0]`, `x[1]` for tuple elements within a comprehension).
- Passing consistent argument counts through recursive calls with many parameters — easy to drop one when a function signature grows.
- Distinguishing `len(grid)` (rows) vs `len(grid[0])` (columns) for non-square 2D structures.

## (3) Key insight / key learning
**Grid problems are graph problems with implicit edges** — instead of an explicit adjacency list, the "edges" are derived on-the-fly from a cell's (row, col) position using direction offsets. The core DFS/traversal logic (visited-tracking, recursive exploration) is identical to explicit-graph DFS (Day 3) — only the neighbor-finding mechanism changes (compute via offsets + bounds-check, instead of looking up an adjacency list).

**Recurring bug pattern identified**: Checking a **value** (`grid[x[0]][x[1]]`, e.g., `'L'`) against a set that's meant to store **positions** (`(row, col)` tuples) is a subtle but easy mistake — the code doesn't crash, it just silently gives wrong results (since `'L' not in visited` is always True if `visited` only ever contains tuples, so the check does nothing useful). This is similar in spirit to Day 4's Path Exists problem's `self.visited` cross-query leak — both are "the check runs, but checks the wrong thing / wrong scope" categories of bugs, which are more dangerous than crashes because they fail silently.

**Square-grid assumption trap**: Defaulting to a single `n` for both dimensions works fine on square grids but silently breaks (or crashes) on rectangular ones — a good habit going forward is to always explicitly get both `rows = len(grid)` and `cols = len(grid[0])` for any 2D grid problem, even if the current test cases happen to be square.

## Time & Space Complexity
- **Time: O(n×m)** — each cell is visited and processed exactly once (guarded by the `visited` check); the 8-direction neighbor check per cell is a constant factor (doesn't scale with n or m), so it drops out of the asymptotic complexity.
- **Space: O(n×m)** — `visited` set can hold up to all cells in the worst case (one giant connected island); recursive call stack can also reach O(n×m) depth in the worst case (e.g., a long zigzag single-file island).

## Connections to earlier learning
- Direct extension of Day 3's DFS pattern (recursive traversal + visited-set) applied to an implicit grid-graph instead of an explicit adjacency list.
- Connects conceptually to Day 4's (deferred) "Connected Components" topic — island-counting IS connected-components-counting on a grid.
- The "check value vs check position" bug pattern echoes Day 4's Path Exists instance-state bug — both are examples of "the logic runs without crashing but checks/tracks the wrong thing."