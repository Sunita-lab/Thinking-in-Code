# Minimum Platforms Required — Concept Notes

**Week:** 9 | Day 3  
**Topic:** Minimum Platforms — interval overlap counting, sweep line technique, relation to Activity Selection

---

## What is Minimum Platforms?

Given arrival and departure times of trains at a station, find the minimum number of platforms required so that no train has to wait — every train that needs a platform at any given moment gets one.

Unlike Activity Selection (which picks a subset of non-overlapping activities to maximize count), this problem requires figuring out **how many things can be happening simultaneously at the busiest point in time** — and every train must be accommodated, none are dropped.

---

## Naive Approach Considered First

Initial instinct was to "group" trains together — pair `arr[i]` with `dep[i]`, then check whether the next train's arrival is before the current train's departure, and if so, lump them into the same group/platform.

**Why this is wrong:** This approach assumed processing trains in their *original order* without first sorting by arrival time. The GFG sample case made this clear:

```
arr[] = [1000, 935, 1100]
dep[] = [1200, 1240, 1130]
```

If pairs are processed as-is `(1000,1200), (935,1240), (1100,1130)` without sorting, train 2 (arriving at 935) would be considered *after* train 1 (arriving at 1000) — even though it actually arrives earlier. Grouping logic breaks immediately without sorting first.

A second, more fundamental misunderstanding was the "grouping" mental model itself — even after sorting by arrival, if two trains overlap, the correct response isn't to "add them to the same group" — it's that they **need separate platforms**, because one platform can only hold one train at a time. The problem isn't about clustering overlapping trains together; it's about **counting how many platforms are simultaneously occupied**.

---

## Sweep Line Technique — Correct Approach

Imagine a scanner moving left to right across the timeline. Every time a train **arrives**, a platform is needed — increment a counter. Every time a train **departs**, a platform is freed — decrement the counter.

The answer is the **maximum value this counter ever reaches** — that represents the busiest moment, i.e., the most platforms needed at any single point in time.

**Manually traced during session** on the sample case (sorted arrivals `935, 1000, 1100`, sorted departures `1130, 1200, 1240`):
- At 935 → counter = 1, max = 1
- At 1000 → counter = 2, max = 2
- At 1100 → counter = 3, max = 3
- Departures happen afterward, counter decreases
- Final answer: 3 ✅ (matches expected output)

---

## Implementation Strategy

1. Combine all arrival and departure events into a single list, tagging each as `'a'` (arrival) or `'d'` (departure).
2. Sort this combined list by time.
3. Walk through chronologically — increment counter on arrival, decrement on departure, track the running maximum.

**Tie-breaking rule (critical):** If an arrival and a departure happen at the exact same time, the platform is **not** considered reusable instantly in this problem's convention — arrival is processed before departure at the same timestamp. This needed to be explicitly enforced in the sort, since sorting only by time doesn't guarantee `'a'` comes before `'d'` when times are equal.

---

## How This Connects to Activity Selection — Similarities and Differences

**Similarities:**
- Both are interval-based problems involving start/arrival and end/departure times.
- Both rely on sorting as the first step to make a greedy/sweep approach valid.
- Both stem from the same underlying theme of Week 9 — reasoning about overlapping time intervals.

**Differences:**

| | Activity Selection | Minimum Platforms |
|---|---|---|
| Goal | Maximize count of activities **selected** (some are dropped) | Accommodate **all** trains — none are dropped |
| What's being optimized | A subset of activities | A resource count (platforms) needed simultaneously |
| Core technique | Greedy — earliest finish time, single pass forward | Sweep line — track simultaneous overlaps via a counter |
| Sort key | Sort by **finish time** only | Sort by **time** across both arrival and departure events combined |
| What happens on overlap | The overlapping activity is simply **skipped/rejected** | The overlapping train still needs a platform — count increases, nothing is rejected |
| Output | A count of selected activities | A count of resources (platforms) needed at peak load |

The fundamental shift is: Activity Selection asks "how many can I fit by being selective," while Minimum Platforms asks "how many resources do I need so I don't have to be selective at all." This is why Activity Selection uses a simple forward greedy scan, while Minimum Platforms needs the sweep line technique to track simultaneous load rather than sequential fit.

---

## Summary

- Minimum Platforms counts maximum simultaneous overlap, not a maximized subset
- The "grouping" naive approach fails — overlapping trains need separate platforms, not the same group
- Sweep line — treat arrivals as +1, departures as -1, track the running maximum
- Sorting must combine both arrival and departure events, with arrival processed before departure on exact time ties
- Structurally different from Activity Selection despite both being interval problems — one selects a subset, the other counts peak concurrent load