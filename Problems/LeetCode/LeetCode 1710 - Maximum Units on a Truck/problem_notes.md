# Maximum Units on a Truck — LC 1710

**Platform:** LeetCode  
**Difficulty:** Easy  
**Topic:** Greedy  
**Week:** 9 | Day 2 (Extra)

---

## Problem

Given `boxTypes` where each entry is `[numberOfBoxes, numberOfUnitsPerBox]` and a `truckSize` (max number of boxes the truck can carry), return the maximum total number of units that can be put on the truck.

---

## Greedy Strategy

Similar to Fractional Knapsack — two attributes interact (number of boxes and units per box). Greedy on either one alone would fail. The correct approach is to prioritize boxes that give the most units per box — sort by `numberOfUnitsPerBox` descending and take as many as possible.

---

## Attempt 1 — Index Out of Range Bug

### Thinking

Built an items list storing `[numberOfBoxes, totalUnits]` for each box type. Sorted by `totalUnits/numberOfBoxes` (units per box) descending. Used a while loop — if all boxes of this type fit, take them all; else take as many as truckSize allows.

### Code

```python
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        items = []
        for i in range(len(boxTypes)):
            items[i] = [boxTypes[i][0], boxTypes[i][0]*boxTypes[i][1]]
        items.sort(key=lambda x: x[1]/x[0], reverse=True)
        i = 0
        maximum = 0

        while truckSize > 0 and i < len(items):
            if items[i][0] <= truckSize:
                maximum += items[i][1]
                truckSize -= items[i][0]
            else:
                maximum += truckSize * (items[i][1]/items[i][0])
                truckSize -= truckSize
            i += 1
        return maximum
```

### Result — Failed (Index Out of Range)

### Bug

`items = []` — empty list. Then `items[i] = ...` tries to assign at index `i` — but empty list has no indices. This throws `IndexError: list assignment index out of range`.

Fix — use `append` instead of index assignment.

---

## Attempt 2 — Fixed, Accepted ✅

### Thinking

Changed `items[i] = ...` to `items.append(...)` — builds the list correctly.

### Code

```python
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        items = []
        for i in range(len(boxTypes)):
            items.append([boxTypes[i][0], boxTypes[i][0]*boxTypes[i][1]])
        items.sort(key=lambda x: x[1]/x[0], reverse=True)
        i = 0
        maximum = 0

        while truckSize > 0 and i < len(items):
            if items[i][0] <= truckSize:
                maximum += items[i][1]
                truckSize -= items[i][0]
            else:
                maximum += truckSize * (items[i][1]/items[i][0])
                truckSize -= truckSize
            i += 1
        return maximum
```

### Result — Accepted ✅

---

## Key Observations

**Fractional case never actually occurs here:**  
The else branch handles the case where remaining `truckSize` is less than available boxes. But since both `truckSize` and `numberOfBoxes` are integers, and `unitsPerBox` is also an integer, the calculation `truckSize * (totalUnits/numberOfBoxes)` always produces an integer result. No true fraction arises from the problem structure — the fractional knapsack template works but the else branch stays in integer territory.

**Connection to Fractional Knapsack:**  
Same ratio-based greedy approach. Two attributes (number of boxes, units per box) interact — greedy on either alone would fail. Ratio (units per box) captures both and is the correct attribute to sort by.

---

## Complexities

| | Time | Space |
|---|---|---|
| Attempt 1 | O(n log n) | O(n) |
| Attempt 2 | O(n log n) | O(n) |

**Time:** Sorting dominates — O(n log n). While loop is O(n).  
**Space:** O(n) for items list.