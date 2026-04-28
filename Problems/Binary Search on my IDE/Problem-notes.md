## Why Left and Right Pointers?
 
In my first attempt, I used `arr[:n//2]` — which created a **new smaller array** on every recursive call.
 
Think about the library analogy — do I actually **move books to a new shelf** to search? No. I just **focus my eyes on the left side**.
 
In code, "eyes focused" = **left and right pointers.**
 
`binary_search(arr, x, left, right)` — same array, only the boundaries change. Creating a new array is wasteful — both memory and time.
 
---
 
## Why is Left > Right the Base Case?
 
When the element doesn't exist in the array, left and right **cross each other**.
 
Example: `arr = [1, 3]`, `x = 2`
- left=0, right=1, mid=0 → arr[0]=1 < 2 → left = 1
- left=1, right=1, mid=1 → arr[1]=3 > 2 → right = 0
- **left=1 > right=0** → stop, return -1
The shelf doesn't become physically "empty" — left and right just cross. That's the signal that the element wasn't found.
 
---
 
## Overflow-safe Mid Calculation
 
```python
mid = left + (right - left) // 2
```
 
Writing `(left + right) // 2` is **technically wrong** in many languages.
 
If `left = 1,000,000,000` and `right = 2,000,000,000` — then `left + right = 3,000,000,000`, which overflows a 32-bit integer (max ~2.1 billion).
 
Python doesn't have this issue (Python integers are unbounded), but in **C++ and Java this is a real bug**. This is a very common interview question.
 
Safe formula: compute the difference first, halve it, then add left. Same result, no overflow.
 
---
 
## Complexities
 
| | Complexity |
|---|---|
| Time | O(log n) |
| Space (recursive) | O(log n) — recursive call stack |
 
**Why O(log n)?**
 
16 books → 4 steps. 1 million books → only 20 steps.
 
Every step cuts n in half — this is the inverse of 2^n, which is **log₂n**.
 
---
 
## Edge Cases
 
- **Element not in array** → when `left > right`, return `-1`
- **Empty array** → handled automatically (`left=0 > right=-1`)

## Recursion vs Iteration
The recursive version is more elegant and easier to understand, but it uses O(log n) space due to the call stack. The iterative version uses O(1) space. In attempt 3, I implemented the iterative version of binary search, which avoids the overhead of recursive calls and uses constant space. The logic remains the same, but instead of calling the function recursively, we use a loop to adjust the left and right pointers until we find the target element or determine that it doesn't exist in the array.