# Linear Search — Problem Notes

## Problem
Given an array and a target element, find all indices where the target occurs.
Handle edge cases: empty array, element not found, multiple occurrences.

## Approach
- Check if array is empty first — if yes, return immediately.
- Traverse the array sequentially.
- Store all matching indices in a list `foundat`.
- After traversal, if `foundat` is non-empty, print indices. Else print not found.

## Complexity
- Time: O(n) — full traversal always needed for all occurrences.
- Space: O(k) — storing k matching indices. Worst case O(n) if all elements match.

## Mistakes & Confusions
- `for...else` was suggested by Copilot — did not fully understand it at the time.
- `for...else` only works with `break` — not applicable here since we need all occurrences.
- **Loop completion tracking doubt:** If loop runs fully but does nothing visible inside, how do we know? 
  Here `foundat` list serves as evidence — empty means loop ran but found nothing.
  General rule: no universal syntax for this — use flag, list, counter, or break depending on the case.

## Key Learning
- `if foundat` is valid — empty list is falsy in Python.
- Tracking loop output vs loop behavior are two different things.
- Designer's choice matters — storing all occurrences costs space, single occurrence with `break` is O(1) space.