# Problem: Two Pointers Technique (Sorted Array) 
**Attempt:** 1  
**Status:** Complete

---

## Problem Statement

Given a sorted array, find two elements whose sum equals a target value.  
Return their indices (or -1, -1 if no such pair exists).

---

## Meri Understanding (apne words mein)

Do markers lagani hai, ek sorted array pe, aur current situation aur target situation ko dynamically compare karte huye dono pointers ya kisi ek ko har step pe adjust karte jana hai jab tak target na mila ya confirm hua ki target nahi milega.

---

## Pehla Thought Process

Pehle socha tha brute force — har element ko har doosre se add karo.  
Jaise `1995 + 1998`, `1995 + 2001`... bahut zyada steps the.  
"Aare baap re" moment aaya jab 14 comparisons ke baad bhi answer nahi mila.

---

## Key Observations Jo Khud Aayi

- Jab `1995 + 2022 = 4017` aaya (target se zyada) — feel hua ki 1995 ke saath aage koi pair nahi banega, kyunki array sorted hai aur 2022 se bada koi element hi nahi
- Agar right end se bhi zyada aa raha hai toh right ko peeche lana padega
- Dono ends se simultaneously move karna padega

---

## Logic (Khud Derive Kiya)

```
left  → index 0       (sabse chhoti value)
right → last index    (sabse badi value)

while left < right:
    current_sum = arr[left] + arr[right]
    
    if current_sum == target  → answer mil gaya
    if current_sum > target   → right ko peeche lao  (sum ghatana hai)
    if current_sum < target   → left ko aage badhao  (sum badhaana hai)
```

**Kyun sorted array zaroori hai?**  
Tabhi guarantee hai ki left side chhoti values hain aur right side badi — tabhi sum predictably control ho sakta hai.

**Ek waqt ek hi pointer kyun?**  
Dono ek saath move karo toh net effect unpredictable — ek badhega ek ghatega, control chala jaata.

---

## Gaps Jo Note Kiye

- **Edge case:** Pehle infinite loop aa gaya — `while current_sum != target_sum` mein `left < right` condition add nahi ki thi
- **Not found case:** While loop 2 cases mein band hoti hai — target mila ya pointers cross ho gaye. Dono cases handle karne the — Copilot ne suggest kiya lekin samjha khud

---

## Final Code

```python
arr = list(map(int, input().split()))
target_sum = int(input())

left, right = 0, len(arr) - 1
current_sum = arr[left] + arr[right]

while left < right and current_sum != target_sum:
    if current_sum < target_sum:
        left += 1
    else:
        right -= 1
    current_sum = arr[left] + arr[right]
else:
    if current_sum == target_sum:
        print(left, right)
    else:
        print(-1, -1)
```

---

## Complexity

| | Brute Force | Two Pointer |
|---|---|---|
| Time | O(n²) | O(n) |
| Space | O(1) | O(1) |

---

## Next Attempt

Attempt 2 gap: +2-3 din  
Focus: Optimized comparison, variations (unsorted array ka kya hoga?)