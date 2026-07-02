# Minimum Number of Moves to Seat Everyone — LC 2037

**Platform:** LeetCode  
**Difficulty:** Easy  
**Topic:** Greedy — Sorted Pairing  
**Week:** 9 | Day 4 (Extra)

---

## Problem

Given `seats[]` and `students[]` arrays of equal length, each student must be moved to a seat. The cost of moving a student is `abs(seats[i] - students[j])`. Return the minimum total number of moves required.

---

## Greedy Strategy (Derived Independently)

Sort both arrays. Pair the i-th smallest seat with the i-th smallest student. Sum up `abs(seats[i] - students[i])` for all pairs.

Intuition — sorting both arrays lets us "face" corresponding seats and students directly in code. Smallest seat pairs with smallest student, largest seat pairs with largest student.

---

## Attempt 1 — Accepted ✅ (First Try)

### Thinking

Sorted both arrays. Used a single loop pairing same-index elements and accumulating absolute differences.

### Code

```python
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        moves = 0
        i = 0
        while i < len(seats):
            moves += abs(seats[i] - students[i])
            i += 1
        return moves
```

### Result — Accepted ✅ (First attempt)

---

## Why Sorted Pairing is Optimal — Exchange Argument

If instead of sorted pairing, any other pairing is used — for example, pairing the smallest seat with the largest student — total moves will be equal or greater, never less.

This is proved by the **exchange argument** — if any two pairs are "crossed" (smallest seat paired with larger student, and largest seat paired with smaller student), swapping them to sorted order never increases total distance. Therefore sorted pairing is globally optimal.

This is the same exchange argument technique used in Boats to Save People (Day 3) — the proof style is identical even though the problems are different. The key difference:

- **Boats to Save People** — minimize number of boats, with a weight constraint (2 people max per boat). Exchange argument proves heaviest + lightest is the optimal pairing.
- **Minimum Moves to Seat** — minimize total distance, no capacity constraint. Exchange argument proves sorted pairing gives minimum total distance.

Constraint presence/absence does not change the proof technique — exchange argument is a general tool that shows "no other pairing can do better than this one."

---

## Complexities

| | Time | Space |
|---|---|---|
| Attempt 1 | O(n log n) | O(1) |

**Time:** Sorting both arrays — O(n log n). Single loop — O(n). Sorting dominates.  
**Space:** O(1) — no extra space used beyond input arrays.