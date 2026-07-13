# Queue — Basic Operations (Concept)

## Derivation Sequence

1. **Motivating scenario:** A single-line ticket counter. If service followed
   Stack (LIFO) order, the most recently arrived person would always be served
   next, and anyone who arrived earlier but is still waiting would never get
   served as long as new people keep arriving — this is **starvation**, the same
   concept that shows up in CPU scheduling when a scheduling policy keeps
   favoring newer/higher-priority processes and indefinitely delays an older one.
2. **Required order:** First-In-First-Out (FIFO) — whoever arrived first should be
   served first.
3. **Two ends, two pointers:** In a Stack, insert and delete both happen at the
   same end, so a single `top` pointer is enough. In a Queue, insertion and
   deletion happen at *different* ends, so two pointers are required:
   - `front` — the end from which deletion (dequeue) happens; points to the
     earliest-arrived, next-to-be-served element.
   - `rear` — the end at which insertion (enqueue) happens.
4. **Empty state convention:** Both `front` and `rear` are initialized to `-1`,
   analogous to `top = -1` in Stack, signaling "no elements yet."
5. **Transition from empty → non-empty:** On the very first enqueue, both
   `front` and `rear` must be set to `0` — not just `rear`. If only `rear` is
   updated, `front` is left at `-1`, which incorrectly still reads as "empty."
6. **Steady-state operations:**
   - `enqueue(x)`: increment `rear`, place `x` at that position.
   - `dequeue()`: increment `front` (element is logically removed, not
     necessarily erased from the array).
7. **Transition from non-empty → empty:** After enough dequeues that every
   enqueued element has been removed, `front` will have overtaken `rear`
   (`front > rear`). This must be explicitly detected and both pointers reset
   to `-1`; otherwise stale pointer values cause future `isEmpty()`/`isFull()`
   checks to be wrong.
8. **Element count formula:** `count = rear - front + 1` (valid when
   `front != -1`) gives the number of elements currently in the queue, and is
   the position-independent way to reason about both `isEmpty` and `isFull`,
   rather than checking `front`/`rear` against fixed positions like `0` or
   `n-1`.

## Misconceptions Caught This Session
- Treating `front == rear` as "empty" — it actually means exactly **one**
  element remains (both pointers point to the same, single remaining element).
  Empty is `front > rear` (after having been valid), or both `== -1` initially.
- Assuming `front` needs to reach `n` (array length) to signal emptiness —
  it doesn't; `front` only needs to overtake `rear`, which can happen well
  before reaching the end of the array.
- Assuming a pointer reaching a fixed array boundary (e.g., `rear == n-1`)
  means the queue is full — this only reflects the array *position*, not the
  actual number of elements present. See `queue_using_array_implementation.md`
  for how this plays out with a plain (non-circular) array.

## Connections to Prior Topics
- Same starvation concept as CPU scheduling (independently drawn by Sunita).
- Contrasts directly with Stack's single-pointer (`top`) design — motivates why
  two pointers are structurally necessary here.