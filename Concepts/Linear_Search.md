# Linear Search

## What is Linear Search?
Linear search is the most basic searching technique. 
You go through each element one by one, sequentially, and check if it matches your target.

**Analogy:** Imagine searching for a book called "Geetanjali" on a bookshelf. 
Starting from the left, I check each book's name one by one. 
I also have a paper where I note down the index of every match I find. 
That sequential process — is linear search.

---

## Edge Cases
- **Empty array:** Nothing to search — return immediately.
- **Multiple occurrences:** If all occurrences are needed, the entire array must be traversed.

---

## Time & Space Complexity

| Case | Complexity | Reason |
|------|------------|--------|
| Best | O(1) | Target found at first position |
| Worst | O(n) | Target at last position or not found |
| Average | O(n) | (best + worst) / 2 |

**Multiple occurrences:** Always O(n) — full array must be traversed no matter what.

**Space Complexity:** O(1) generally — no extra space used during search.
If storing all occurrences (e.g. in a list), space becomes O(k) where k = number of matches. This is a designer's choice.

---

## Applications
- **Unsorted lists:** Most commonly used when array is unsorted.
- **Small data sets:** Preferred over binary search for small collections.
- **Linked lists:** Each node checked sequentially until target is found.
- **Simple implementation:** Much easier to understand and implement compared to Binary Search or Ternary Search.