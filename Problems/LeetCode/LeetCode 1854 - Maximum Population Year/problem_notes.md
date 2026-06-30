# Maximum Population Year — LC 1854

**Platform:** LeetCode  
**Difficulty:** Easy  
**Topic:** Greedy — Sweep Line  
**Week:** 9 | Day 3 (Extra)

---

## Problem

Given `logs[]` where each entry is `[birth, death]` representing a person's birth and death year, find the year with the maximum population. If there are multiple years with the same maximum population, return the earliest one. A person is **not counted** in the population during their death year.

---

## Pre-Coding Thinking

Recognized this as a direct application of the sweep line technique learned in Min Platforms — births act as `+1` events, deaths act as `-1` events, and the year with maximum cumulative count is the answer.

---

## Attempt 1 — Wrong Tie-Breaking Order (Birth Before Death)

### Thinking

Built a combined `times` list tagging each birth as `'b'` and each death as `'d'`. Sorted using `key=lambda x: (x[0], x[1])` — since `'b' < 'd'` alphabetically, this processed births before deaths when years tied. Tracked a running `count` and `maximum`, and recorded `[year, count]` pairs for every year to later find the earliest year hitting the maximum.

### Code

```python
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        times = []
        maxforyears = []
        for i in range(len(logs)):
            times.append([logs[i][0], 'b'])
            times.append([logs[i][1], 'd'])

        times.sort(key=lambda x: (x[0], x[1]))
        maximum = 0
        count = 0
        i = 0
        while i in range(len(times)):
            if times[i][1] == 'b':
                count += 1
            else:
                count -= 1
            maximum = max(maximum, count)
            maxforyears.append([times[i][0], count])
            i += 1
        earliest = min([x for x in maxforyears if x[1] == maximum])
        return earliest[0]
```

### Result — 35/53 test cases passed

**Failing case:**
```
logs = [[2008,2026],[2004,2008],[2034,2035],[1999,2050],[2049,2050],[2011,2035],[1966,2033],[2044,2049]]
Output: 2008, Expected: 2011
```

### Bug — Death Should Be Processed Before Birth on a Tie

The problem explicitly states a person is **not counted in their death year**. This means if a birth and a death happen in the same year, the death's effect (`-1`) must be applied **before** the birth's effect (`+1`) — otherwise the death year incorrectly retains the population of the person who died, inflating the count for that year.

The sort `'b' < 'd'` processed births first, which is the opposite of what's needed here — this is the reverse of the Min Platforms problem, where arrival (equivalent to birth) needed to be processed *before* departure on a tie. Here, death needs priority over birth on a tie, because of how the problem defines "not counted in death year."

---

## Attempt 2 — Death Tagged to Sort Before Birth, Accepted ✅

### Thinking

Needed deaths to be processed before births when years are equal. Since `'b' < 'd'` alphabetically gave the wrong order, the death tag was changed to a character that sorts before `'b'` alphabetically (e.g., `'a'`), forcing deaths to be processed first in a tie.

### Code

```python
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        times = []
        maxforyears = []
        for i in range(len(logs)):
            times.append([logs[i][0], 'b'])
            times.append([logs[i][1], 'a'])  # death tagged 'a' so it sorts before birth ('b')

        times.sort(key=lambda x: (x[0], x[1]))
        maximum = 0
        count = 0
        i = 0
        while i in range(len(times)):
            if times[i][1] == 'b':
                count += 1
            else:
                count -= 1
            maximum = max(maximum, count)
            maxforyears.append([times[i][0], count])
            i += 1
        earliest = min([x for x in maxforyears if x[1] == maximum])
        return earliest[0]
```

### Result — Accepted ✅

---

## Key Learning — Reusable Tie-Breaking Pattern

This connects directly to the Min Platforms problem (same week, same day). Both problems needed event-based tie-breaking using a tuple sort key `(time, tag)`, where the tag character is deliberately chosen so its alphabetical order enforces the correct processing sequence:

- **Min Platforms:** arrival needed to process before departure on a tie → tag arrival `'a'`, departure `'d'` (`'a' < 'd'` naturally worked).
- **Maximum Population Year:** death needed to process before birth on a tie → original tags `'b'` (birth) and `'d'` (death) had the wrong relative order, so death was retagged to `'a'` to force it first.

**General pattern derived:** when two types of events can occur at the same timestamp and order matters, pick tag characters specifically so that alphabetical (or numeric) ordering of the tag enforces the required processing priority — don't assume default tag names will sort correctly; verify and adjust deliberately.

---

## Complexities

| | Time | Space |
|---|---|---|
| Attempt 1 | O(n log n) | O(n) |
| Attempt 2 | O(n log n) | O(n) |

**Time:** Sorting `2n` combined birth/death events dominates at O(n log n).  
**Space:** O(n) for the `times` list and `maxforyears` list, both holding up to `2n` entries.