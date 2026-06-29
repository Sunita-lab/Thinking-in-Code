# Two Pointer Technique
**First encountered:** Two Pointers (Sorted Array)

---

## Apni Understanding

Do markers lagani hai, ek sorted array pe, aur current situation aur target situation ko dynamically compare karte huye dono pointers ya kisi ek ko har step pe adjust karte jana hai jab tak target na mila ya confirm hua ki target nahi milega.

---

## Intuition — Ye Kyun Exist Karta Hai

Brute force mein har element ko har doosre se compare karo — O(n²).  
But agar array **sorted** hai, toh ek smart observation hai:

- Sabse chhoti + sabse badi = already ek extreme sum
- Agar ye sum target se zyada hai → badi wali ghatao (right peeche)
- Agar ye sum target se kam hai → chhoti wali badhao (left aage)
- Har step pe ek element eliminate ho jaata hai → O(n)

Brute force ka "aare baap re" moment jab 14 comparisons pe bhi answer nahi mila 10-element list mein — wahi Two Pointer ka janm tha.

---

## Core Pattern

```
left  = 0           ← array ka start
right = n - 1       ← array ka end

while left < right:
    evaluate(arr[left], arr[right])
    
    if condition_to_shrink_right:
        right -= 1
    elif condition_to_grow_left:
        left += 1
    else:
        # answer found
```

---

## Zaroori Conditions

**Sorted array kyun chahiye?**  
Tabhi predictable hai ki left badhane se sum badhega aur right ghatane se sum ghatega.  
Unsorted mein ye guarantee nahi → Two Pointer kaam nahi karega directly.

**Ek waqt ek hi pointer kyun?**  
Dono simultaneously move karo → net effect unpredictable → control chala jaata.

**left < right kyun?**  
Jab dono cross ho jaayein → koi valid pair nahi bacha → loop band karo.

---

## Complexity

| | Time | Space |
|---|---|---|
| Two Pointer | O(n) | O(1) |
| Brute Force | O(n²) | O(1) |

---

## Representative Problems

| Problem | Platform | Status |
|---|---|---|
| Two Sum (Sorted Array) | LeetCode 167 | Attempt 1 ✅ |

---

## Common Misconceptions

- "Unsorted array pe bhi kaam karega" → Nahi, sorted hona zaroori hai (ya pehle sort karo)
- "Dono pointers ek saath move karo" → Net effect unpredictable ho jaata hai

---

## Variations (Baad Mein Aayengi)

- Three Sum
- Sliding Window (related concept — Week 7)
- Dutch National Flag problem
- Palindrome check

---

*Last updated: Week 7, Day 1 | Attempt 1 complete*