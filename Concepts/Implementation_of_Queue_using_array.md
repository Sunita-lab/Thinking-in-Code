# Queue using Array — Implementation (Concept)

## Derivation Sequence

1. Start from the basic operations model (`front`, `rear`, both `-1` when
   empty; see `queue_basic_operations.md`).
2. **The wasted-space problem:** Consider a fixed-size array queue where
   elements have been enqueued and then some dequeued. `front` moves forward
   as elements are removed, but the array slots before the current `front`
   are never reused — only `rear` moving forward makes new slots usable.
   Example: array size 5, `front=0, rear=4` (full). Dequeue twice → `front=2`,
   but indices `0` and `1` are now permanently unusable in this design, even
   though only 3 elements remain and there's real leftover capacity.
   Consequence: `rear` can hit the last valid index (`n-1`) while the queue is
   nowhere near logically full — this is what motivates Circular Queue later,
   where `rear` wraps back around to index `0` instead of being stuck.
3. **`isFull` — the naive-but-wrong version:** Checking `rear == n - 1` only
   tests whether `rear` has reached the last array index. This conflates
   "array position exhausted" with "queue logically full," and is wrong
   whenever dequeues have happened and left unused space at the front.
4. **`isFull` — the patch trap:** Adding an extra condition like
   `front == 0` to the above check can make a specific failing test pass,
   because it happens to match the exact pointer configuration in that test.
   But it doesn't generalize — a different configuration (e.g.
   `front=1, rear=n-1`, where the queue is genuinely not full) will still be
   misclassified. This is a **patch**: it fixes the symptom seen, not the
   underlying relationship.
5. **`isFull` — the robust version:** Use the same element-count formula
   derived in basic operations: `count = rear - front + 1`. The queue is full
   exactly when `count == n`. This depends only on the actual number of
   elements present, not on where `front`/`rear` happen to sit in the array —
   so it holds for every configuration, not just the ones tested so far.
6. **General principle (patch vs. robust solution):** A patch reacts to one
   observed failure and narrows the fix to that shape of input; it can pass
   visible tests by coincidence. A robust solution is derived from the actual
   invariant governing the structure (here, the count relationship between
   `front` and `rear`), so correctness doesn't depend on which test cases
   happen to be checked.

## Misconceptions Caught This Session
- Believing `rear` reaching the last index always means "full" — true only
  for a queue that has never had a dequeue; false in general.
- Believing a fix that passes the given test suite is necessarily correct —
  passing tests is evidence, not proof; a fix should be checked against the
  underlying invariant, not just against the cases that happened to be run.

## Connections to Prior Topics
- Same "give the empty/boundary case an explicit, uniform rule" spirit as the
  sentinel/dummy-node principle Sunita identified in Linked Lists and in
  Stack problems (Score of Parentheses, Stock Span) — here the rule is
  "compute count from `front`/`rear` directly" rather than special-casing
  positions.
- Sets up the motivation for **Circular Queue** (Day 3): wraparound exists
  specifically to eliminate the wasted-space problem described in step 2.

## Complexity
- All core operations (`enqueue`, `dequeue`, `isEmpty`, `isFull`, `getFront`,
  `getRear`) are O(1) time.
- Space: O(n) for the fixed-capacity array.