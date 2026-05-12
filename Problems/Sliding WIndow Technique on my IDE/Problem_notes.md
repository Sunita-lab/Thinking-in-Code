# Sliding Window — On VS Code



## Important Edge Cases

**Loop range:**
```
range(len(arr) - k)   ← second loop ke liye sahi
```
`len(arr) - k + 1` total windows count ke liye sahi hai — par second loop mein `a[i+k]` access hoti hai, toh `+1` lagao toh IndexError.


## Kab Use Karna Hai

Jab problem mein ho:
- "k consecutive elements"
- "subarray of size k"
- "window of length k"

Aur tum kuch track kar rahe ho us window mein — sum, average, count, max, min.

---


## Attempt Log

| Attempt | Date | Notes |
|---|---|---|
| Attempt 1 | May 2026 | Fixed window derive kiya — gharon ka sum problem se. O(n) reasoning khud ki. |

---

*Slow is smooth. Smooth is fast.*