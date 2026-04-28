# Binary Search
 
## What is it?
 
A searching technique that works **only on sorted arrays**.
 
The idea is simple — if an array is sorted, we can start from the middle and eliminate **half the array in a single comparison**.
 
---
 
## Intuition — The Library Example
 
Imagine a library where books are arranged alphabetically. I need to find **Gitanjali**.
 
I won't start from A — that wastes time. I'll pick the **shelf in the middle**.
 
Say the middle gives me **K**. Gitanjali (G) comes before K — so I'll search **only the left half** now. Right half is ignored forever.
 
The left half becomes my new "library." I pick the middle again. This continues until Gitanjali is found — or confirmed to not exist.
 
**Key insight:** Every step cuts the search space in **half**. No need to go all the way to the end.
 
 ## Complexities
 
| | Complexity |
|---|---|
| Time | O(log n) |
| Space (recursive) | O(log n) — recursive call stack |
| Space (iterative) | O(1) — constant space |

## Edge Cases
 
- **Element not in array** → when `left > right`, return `-1`
- **Empty array** → handled automatically (`left=0 > right=-1`)