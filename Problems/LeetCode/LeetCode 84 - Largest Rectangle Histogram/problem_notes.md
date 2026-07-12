# Problem: LC 84 — Largest Rectangle in Histogram (Hard)
## Link - https://leetcode.com/submissions/detail/2065037239/

## Problem statement
Ek histogram diya hai — bars ki ek series, har bar ki ek height, sab bars ki width samaan (1 unit). Histogram ke andar aane wala sबसे bada rectangle (area ke hisab se) dhundhna hai.

## Approach — sequence jaisa socha

### Pehla challenge — problem ko "monotonic stack ki problem" ke roop mein pehchanna
Shuru mein turant clear nahi tha ki ye monotonic stack se solve hoga — problem-statement mein koi seedha "stack" wala signal nahi tha (jaisa NGE ya Stock Span mein tha, jahan "next greater" jaisa direct cue milta hai). Ye decomposition se aaya.

### Decomposition — ek bar ko fix karke socha
Concrete example (`[2,1,5,6,2,3]`) pe socha: agar ek particular bar (jaise height `6`, index 3) ko rectangle ki height maan lein, to uski **width** kितनी ho sakti hai — matlab kितने consecutive bars (is bar ke aas-paas) uski height se **kam nahi** hain.

Trace kiya `6` ke liye: left mein `5` (chhota, rukna hai), right mein `2` (chhota, rukna hai) → width sirf `1`.

Trace kiya `5` (index 2) ke liye: pehle **galti se** left mein "koi nahi" bola (jabki actual mein index 1 pe `1` hai jo `5` se chhota hai — ye **Previous Smaller** hai, na ki "koi nahi"). Is galti se realize hua ki confusion "Previous Greater" aur "Previous Smaller" ke beech thi — is problem ko chahiye **Previous Smaller** aur **Next Smaller**, kyunki rectangle tab tak फैल sakta hai jab tak koi bar **chhota** na mile (bada bar to us height ko "support" kar sakta hai).

### Connection jo bani — Previous/Next Smaller Element
Realize kiya ki ye poora problem **Previous Smaller Element** aur **Next Smaller Element** (jo poore week mein derive kiye gaye concepts hain) ka application hai — har bar ke liye:
- `left[i]` = Previous Smaller ka index (jahan tak left mein फैल sakte hain)
- `right[i]` = Next Smaller ka index (jahan tak right mein फैल sakte hain)
- `width = right[i] - left[i] - 1`
- `area = height[i] * width`
- Answer = max area sab bars mein se

### Sentinel-values dono directions ke liye (naya insight)
Socha: agar `left[i]` ka sentinel `-1` hai ("index se ek pehले"), to `right[i]` ka sentinel bhi ussi tarah "index ke ek baad" hona chahiye — na ki bhi `-1` (jo confusion create karta, kyunki `-1` already left-side ke liye reserved hai). Derive kiya ki right ka sentinel = **array length `n`** (jo "last valid index se ek aage" represent karta hai, `-1` jaisa hi ek "array ke bahar" ka marker, bas doosri taraf).

Verify kiya `[2,2]` (duplicate heights) jaise example se ki dono sentinels sahi combination mein sahi max-area deते hain.

### Duplicate values ka handling — `>=` ka istemal
Sawaal utha: discard-condition mein `>` (strictly greater) use karein ya `>=` (greater-or-equal)? Concrete trace kiya `[2,2]` pe — `>=` use karke dono directions mein, **dono bars ne independently sही max-area (`4`) capture kar liya**, koi galat/kam area nahi aaya. Confirm hua ki `>=` (equal ko bhi discard karna) is problem ke liye safe hai, dono traversals mein.

## Attempt 1 — do bugs, dono fix hue

```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left = [-1]*len(heights)
        right = [len(heights)]*len(heights)
        stack1 = []
        stack2 = []
        areas = []*(len(heights))
        for i in range(0, len(heights)):
            while stack1 and stack1[-1] >= heights[i]:
                stack1.pop()
            left[i] = stack1[-1] if stack1 else -1
            stack1.append(i)
        for i in range(len(heights) - 1, -1, -1):
            while stack2 and stack2[-1] >= heights[i]:
                stack2.pop()
            right[i] = stack2[-1] if stack2 else len(heights)
            stack2.append(i)
        for i in range(0, len(heights)):
            areas[i] = heights[i] * (right[i] - left[i] - 1)
        return max(areas)
```

**Bug A — stack mein index push kiya, lekin comparison value se kiya**: `while stack1 and stack1[-1] >= heights[i]:` — `stack1[-1]` ek **index** hai (jaisa `2`), lekin ise seedha `heights[i]` (ek height-value, jaisa `5`) se compare kiya — apples-to-oranges comparison. Fix: `heights[stack1[-1]] >= heights[i]` — index se pehle uski **height** nikalni thi, phir compare karna tha.

**Bug B — `[] * n` khali list hi rehti hai**: `areas = []*(len(heights))` — socha tha ki ye `n` elements ki list banayega, lekin **khali list ko kितna bhi multiply karo, khali hi rehti hai** (`[0]*n` se `n` zeros ki list banti, `[]*n` se khali list). Baad mein `areas[i] = ...` karne ki koshish crash karti (IndexError, khali list pe index-assignment). Fix: `areas = [0]*len(heights)` — sही tareeka jisse fixed-size list pre-allocate hoती hai.

## Fix (final)
```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = [-1]*n
        right = [n]*n
        stack1 = []
        stack2 = []
        areas = [0]*n
        for i in range(n):
            while stack1 and heights[stack1[-1]] >= heights[i]:
                stack1.pop()
            left[i] = stack1[-1] if stack1 else -1
            stack1.append(i)
        for i in range(n - 1, -1, -1):
            while stack2 and heights[stack2[-1]] >= heights[i]:
                stack2.pop()
            right[i] = stack2[-1] if stack2 else n
            stack2.append(i)
        for i in range(n):
            areas[i] = heights[i] * (right[i] - left[i] - 1)
        return max(areas)
```
Submit kiya, accepted.

## Key learning
- Hard problems mein "kaunsi technique lagegi" ka signal seedha nahi milta — problem ko **decompose karke** (jaise "ek element fix karke, uske around ka span dhundo") chhote, familiar-pattern-tak pahunchna padta hai. Ye normal aur expected hai, weakness nahi.
- **Sentinel-values dono directions ke liye alag hone chahiye** (`-1` left ke liye, `n` right ke liye) — dono ek hi value (`-1`) nahi ho sakte, warna formula confuse ho jata hai kis direction ka "kuch nahi mila" represent kar raha hai.
- **Duplicate values ke liye `>=` ka istemal** — test karke (concrete `[2,2]` example se) confirm kiya ki equal-height bars ko bhi discard karna, is problem mein galat/kम area nahi deता, balki sही max-area capture karता hai dono directions mein.
- **Index vs value confusion** — jab stack mein indices store karte ho (jo is course mein baar-baar hone wala pattern hai — Stock Span, NGE-mapping mein bhi), comparison hamesha `heights[stack[-1]]` se karna hai, `stack[-1]` se seedha nahi.
- `[] * n` aur `[0] * n` mein bahut bada farak hai — khali list ko multiply karne se khali hi rehти hai, list pre-allocate karne ke liye placeholder-value (`0`, ya `-1`, jo bhi sही ho) wali list use karni chahiye.

## Complexity
- Time: O(n) — do alag monotonic-stack passes, dono amortized O(n)
- Space: O(n) — do stacks, `left[]`, `right[]`, `areas[]`