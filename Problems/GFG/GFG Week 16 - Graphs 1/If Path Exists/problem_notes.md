# Problem: Path Exists Between Two Vertices (GFG "checkPath" + LC 1971 "Find if Path Exists in Graph" — EXACT MATCH)

**Week 16 — Day 4 — Path & Connectivity**

## Problem Statement
Undirected graph diya hai (`V` vertices, `edges`). Check karo — kya `src` se `dest` tak koi path exist karta hai (chahe directly ho ya multiple hops se).

## Concept Connection
"Path exists" ka matlab hai: `src` se DFS/BFS karo, dekho `dest` reachable hai ya nahi. Do approaches discuss kiye:
- Poora traversal complete karke phir check karna (less efficient)
- **Early exit** — jaise hi `dest` mil jaaye turant `True` return karna (better average-case, same worst-case O(V+E))

## My Approach — iterative debugging (5 versions), THREE distinct bugs found

### Version 1 (WRONG — fixed 2-hop check, not real traversal)
```python
class Solution:
    def check(self, src, dest, li):
        if dest in li[src]:
            return True
        return False
    def checkPath(self, V, edges, src, dest):
        if dest == src:
            return True
        adj = [[] for _ in range(V)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        if dest not in adj[src]:
            for i in range(len(adj[src])):
                if self.check(adj[src][i], dest, adj):
                    return True
        return False
```
**Bug**: Sirf **2 levels deep** tak check kar raha tha (src ke direct neighbors, aur unke neighbors) — general traversal nahi tha. Traced with `edges=[[0,1],[1,2],[2,3]]`, `src=0,dest=3` (3 hops away) — returned `False` incorrectly kyunki 3-hop paths cover hi nahi ho rahe the.

### Version 2 (DFS pattern reused, but return value not propagated)
```python
def check(self, src, dest, adj):
    self.visited.add(src)
    for i in range(len(adj[src])):
        if adj[src][i] == dest:
            return True
        if adj[src][i] not in self.visited:
            self.check(adj[src][i], dest, adj)   # BUG: return value discarded
```
**Bug**: Recursive call ka return value (`True`/`False`/`None`) kahin store/return nahi ho raha tha — bas call ho raha tha aur result discard ho raha tha. Isse deep-path cases mein `True` mil ke bhi wo signal upar propagate nahi hota tha.

### Version 3 (over-corrected — unconditional return broke sibling exploration)
```python
if adj[src][i] not in self.visited:
    return self.check(adj[src][i], dest, adj)   # BUG: always returns after FIRST unvisited neighbor
```
**Bug**: `return` add kiya, lekin **unconditionally** — isse loop **turant** ruk jaata tha pehle hi unvisited neighbor pe, chahe wo path False de. Baaki neighbors (jinmein se ek directly `dest` ho sakta tha) kabhi check hi nahi hote the. Traced with branching graph (`adj[0]=[1,3]`, dest=3): loop `i=0` pe hi `return self.check(1, 3, adj)` chal gaya, aur `i=1` (`adj[0][1]=3`, jo actual answer tha) kabhi reach hi nahi hua.

### Version 4 (conditional return — correct core logic, but missing final return)
```python
def check(self, src, dest, adj):
    self.visited.add(src)
    for i in range(len(adj[src])):
        if adj[src][i] == dest:
            return True
        if adj[src][i] not in self.visited:
            res = self.check(adj[src][i], dest, adj)
            if res == True:
                return True
    # BUG: missing `return False` here — falls through to implicit None
```
Core logic sahi ho gaya (store result in `res`, conditionally return True), lekin function ke end mein explicit `return False` missing tha — agar loop pura complete ho jaaye bina True mile, function implicitly `None` return karta. `None` Python mein falsy hai isliye `if self.check(...)` wale checks mein by-luck kaam kar jaata, lekin fragile/risky tha (explicit `== False` comparisons mein `None == False` is actually `False`, potential future bug).

### Version 5 (added `return False`, but STILL failed on GFG — cross-query state leak)
```python
class Solution:
    def __init__(self):
        self.visited = set()
    def check(self, src, dest, adj):
        self.visited.add(src)
        for i in range(len(adj[src])):
            if adj[src][i] == dest:
                return True
            if adj[src][i] not in self.visited:
                res = self.check(adj[src][i], dest, adj)
                if res == True:
                    return True
        return False
    def checkPath(self, V, edges, src, dest):
        if dest == src:
            return True
        adj = [[] for _ in range(V)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        if self.check(src, dest, adj):
            return True
        return False
```
GFG pe 13 test cases pass, but ek specific input pe fail: `V=4`, edges `0-1, 0-3, 1-2`, **3 separate queries** in same test, ek query `src=3, dest=2` expected `True` but got `False`.

**Root cause**: `self.visited` **instance attribute** thi (`__init__` mein banayi), aur GFG **ek hi `Solution` object** pe **multiple queries sequentially** chalata hai. Pehli query ke baad `self.visited` mein purane nodes reh gaye — jab **doosri query** shuru hui, `self.visited` **already partially filled** thi (fresh nahi thi), isliye code galti se soch raha tha ki kuch nodes already visited hain jabki naye query context mein unhe fresh se explore karna chahiye tha.

### Version 6 — FINAL FIX (visited as local variable, passed explicitly)
```python
class Solution:
    def check(self, src, dest, adj, visited):
        visited.add(src)
        for i in range(len(adj[src])):
            if adj[src][i] == dest:
                return True
            if adj[src][i] not in visited:
                res = self.check(adj[src][i], dest, adj, visited)
                if res == True:
                    return True
        return False
    def checkPath(self, V, edges, src, dest):
        if dest == src:
            return True
        adj = [[] for _ in range(V)]
        visited = set()   # fresh, LOCAL to this call
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        if self.check(src, dest, adj, visited):
            return True
        return False
```
`visited` ab **local variable** hai `checkPath` ke andar, har call ke liye fresh — aur explicitly parameter ke through `check` mein pass hoti hai, `self.visited` nahi. **Accepted, all test cases pass.**

## (1) Mid-way doubts

- **Fixed-depth vs full-traversal confusion**: Pehla attempt sirf 2-hop tak check kar raha tha, samajh nahi aaya tha ki general path-existence ke liye **poori depth tak** traversal chahiye, na ki fixed number of hops.
- **Return value propagation ka concept**: Recursive call ka result "automatically" upar nahi jaata jab tak explicitly `return` na kiya jaaye — ye clear nahi tha shuru mein.
- **Unconditional vs conditional return ka trap**: `return self.check(...)` likhna aur `res = self.check(...); if res: return True` likhna — inka fark samajhna padha trace karke, kyunki unconditional return se **sibling exploration break** ho jaata hai.
- **Implicit `None` return ka risk**: Function ke end mein explicit `return False` na hone se function chup-chaap `None` return karta hai — Python mein `None` falsy hai isliye kaam chal jaata hai `if` checks mein, lekin best practice nahi hai.
- **Biggest doubt — instance attribute (`self.visited`) vs local variable ka cross-query leak**: Ye sabse subtle bug tha. Code manually traced karne pe (single query ke liye) bilkul sahi lagta tha, lekin GFG pe multiple queries (same Solution object pe) ke saath fail ho raha tha. Root cause samajhna padha ki `self.__init__` sirf **ek baar** chalta hai jab Solution object banta hai, uske baad saari queries **same instance attributes share karti hain** jab tak explicitly reset na karo.

## (2) Syntax / Python concepts touched
- Recursive return-value propagation — `return self.func(...)` vs storing in variable then conditionally returning.
- Implicit `None` return when a function has no explicit `return` on all code paths.
- **Instance attributes (`self.x` in `__init__`) persist across multiple method calls on the same object** — critical when a platform (GFG) reuses one `Solution` instance for multiple test queries. Local variables (declared fresh inside a method) don't have this problem.

## (3) Key insight / key learning

**Sabse important insight — Instance state vs. per-call state**: Jab ek class attribute (`self.visited`) `__init__` mein banaya jaata hai, wo us **Solution object ki poori lifetime** tak persist karta hai — agar platform (jaise GFG) **ek hi object pe multiple independent queries** chalata hai, to purane query ka leftover state naye query ko silently corrupt kar sakta hai. **Jo bhi state ek single call/query ke liye specific honi chahiye (jaise visited-tracking for one particular path-check), use local variable ke roop mein banao aur explicitly pass karo — `self` attribute mat banao, jab tak genuinely poori object lifetime tak persist karne ki zaroorat na ho.**

Ye Day 3's DFS/BFS problems se ek subtle difference hai — un problems mein `self.visited` kaam kar gaya tha kyunki wahan **ek hi call** hoti thi function ki (ek hi traversal). Yahan **multiple independent queries** the same object pe, jisse cross-query contamination ka naya risk aaya jo pehle nahi dekha tha.

## Concrete Trace — the final bug (cross-query state leak)

Input: `V=4`, edges: `0-1, 0-3, 1-2`. Query 1 runs first (some src,dest), then Query 2: `src=3, dest=2`.

**Buggy version (`self.visited` as instance attribute)**:
- Query 1 runs `self.check(...)`, adds some nodes to `self.visited` (e.g., ends up with `self.visited` containing leftover nodes from query 1).
- Query 2 starts: `self.check(3, 2, adj)` — but `self.visited` is **not empty** — it already has nodes from query 1's traversal.
- If query 1 happened to touch node `2` or `1` or `3`, query 2's traversal will incorrectly skip them (`if adj[src][i] not in self.visited` → wrongly True/False due to stale state), leading to wrong `False` even though a path exists.

**Fixed version (local `visited`)**:
- Query 2's `checkPath` call creates `visited = set()` — completely fresh, no memory of query 1.
- `self.check(3, 2, adj, visited)` traverses cleanly: `visited={3}` → neighbor 0 → `visited={3,0}` → neighbor 1 → `visited={3,0,1}` → neighbor 2 → `2 == dest` → `True`. Correct result.

## Time & Space Complexity
- **Time: O(V + E)** — standard DFS traversal complexity, same pattern as Day 3.
- **Space: O(V)** — `visited` set (O(V)) + recursive call stack (worst case O(V)).

## Connections to earlier learning
- Reuses Day 3's DFS + visited-set pattern directly.
- Early-exit optimization concept — discussed before implementation, applied via conditional `return True` once `dest` found.
- New, platform-specific lesson (not seen in Day 1-3 problems): **multiple test queries on one Solution instance** — a consideration specific to how GFG (and possibly other platforms) structure their test harness, requiring care about instance vs. local state that wasn't relevant when each problem had a single invocation.