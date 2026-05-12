# Sliding Window — On VS Code

## Resistance  — Copilot ka wrong suggestion

Copilot ne second loop mein `range(len(nums) - k + 1)` suggest kiya.

**Kya hota agar lagaate:** `i = len(nums)-k` pe `nums[i+k] = nums[len(nums)]` — IndexError.

**Confusion:** `len(a) - k + 1` mathematically sahi hai total windows count ke liye. Par loop mein `a[i+k]` access hoti hai — wahan ek kam chahiye.

```
Total windows     = n - k + 1   ← count ke liye
Second loop range = n - k       ← indexing ke liye
```

Khud reason karke fix kiya — Copilot pe blindly nahi gaye.

---




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