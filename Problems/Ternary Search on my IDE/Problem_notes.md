# Problem: Peak Element in Unimodal Array (Ternary Search)
 
**Topic:** Ternary Search — Week 6
**Difficulty:** Easy-Medium
**Status:** Working (edge case pending)
 
---
 
## Problem Statement
 
Ek unimodal array diya hai — pehle badhta hai, phir ghatta hai. Peak element dhundo.
 
```
Input:  [1, 3, 7, 12, 18, 23, 19, 14, 8, 3]
Output: 23 at index 5
```
 
---
 
## Approach
 
Ternary search — array ko 3 parts mein todna, mid1 aur mid2 ke values compare karke region eliminate karna. Target ki value pata nahi hoti — isliye binary search ka direct comparison nahi kaam karta.
 
---
 
## starter: attempt1 — Infinite Loop, Wrong Formula
 
```python
def ternary_search(arr):
    left, right = 0, len(arr)-1
    mid = (left + right) // 2
    while left != right:
        mid1 = (left + mid) // 2
        mid2 = (right + mid) // 2
        if mid1 < mid2:
            left = mid1
        elif mid1 > mid2:
            right = mid2
        else:
            left = mid1
            right = mid2
    else:
        return left
```
 
**Kya hua:** Terminal hang — infinite loop.
 
**Kya galat tha:**
- `mid` ki zaroorat hi nahi thi — mid1 aur mid2 directly left aur right se nikalte hain
- `mid1 < mid2` — indices compare kar raha tha, values nahi (`arr[mid1]` hona chahiye tha)
- `left = mid1` — index assign karna chahiye tha, value nahi
- Pointers update nahi ho rahe the properly — isliye loop kabhi nahi rukta tha
 
---
 
## Refinement 2 — IndexError, Indices vs Values Confusion
 
```python
def ternary_search(arr):
    left, right = 0, len(arr)-1
    while left != right:
        mid1 = (left + right) // 3
        mid2 = ((right + left) // 3) * 2
        if arr[mid1] < arr[mid2]:
            left = arr[mid1 + 1]   # ← IndexError yahan
        elif arr[mid1] > arr[mid2]:
            right = arr[mid2 - 1]
        else:
            left = arr[mid1 + 1]
            right = arr[mid2 - 1]
    else:
        return left
```
 
**Kya hua:** IndexError.
 
**Kya galat tha:**
- `left = arr[mid1 + 1]` — `left` ek **index** hona chahiye, `arr[...]` **value** deta hai
- Fix: `left = mid1 + 1`
- Mid formula bhi galat tha — `(left + right) // 3` left ko consider nahi karta properly
 
---
 
## Refinement 3 — Infinite Loop, Wrong Mid Formula
 
```python
def ternary_search(arr):
    left, right = 0, len(arr)-1
    while left != right:
        mid1 = (left + right) // 3
        mid2 = ((right + left) // 3) * 2
        if arr[mid1] < arr[mid2]:
            left = mid1 + 1
        elif arr[mid1] > arr[mid2]:
            right = mid2 - 1
        else:
            left = mid1 + 1
            right = mid2 - 1
    else:
        return left
```
 
**Kya hua:** Phir bhi infinite loop.
 
**Kya galat tha:**
- Mid formula: `(left + right) // 3` — yeh left ko base nahi banata. Jab left = 4, right = 8:
  - mid1 = 4, mid2 = 8 — same as before, koi progress nahi
- Sahi formula: `m = (right - left + 1) // 3`, phir `mid1 = left + m`, `mid2 = right - m`
 
---
 
## Refinement 4 — Equal Case Bug
 
```python
def ternary_search(arr):
    left, right = 0, len(arr)-1
    while left != right:
        m = (right - left + 1) // 3
        mid1 = left + m
        mid2 = right - m
        if arr[mid1] < arr[mid2]:
            left = mid1 + 1
        elif arr[mid1] > arr[mid2]:
            right = mid2 - 1
        else:
            left = mid1 + 1   # ← bug
            right = mid2 - 1  # ← bug
    else:
        return left
```
 
**Kya hua:** Kuch arrays pe `left > right` ho jaata tha — loop kabhi nahi rukta.
 
**Kya galat tha:**
- Equal case mein `mid1 + 1` aur `mid2 - 1` — jab mid1 == mid2 ho toh left right se aage chala jaata hai
- Equal case mein peak **mid1 aur mid2 ke beech** hoti hai — toh `left = mid1`, `right = mid2` hona chahiye (without +1/-1)
 
---
 
## final — Working Solution (till attempt1 end)
 
```python
print("Enter the elements of the unimodal array: ")
arr = list(map(int, input().split()))
 
def ternary_search(arr):
    left, right = 0, len(arr) - 1
    
    while left != right:
        m = (right - left + 1) // 3
        mid1 = left + m
        mid2 = right - m
        
        if arr[mid1] < arr[mid2]:
            left = mid1 + 1
        elif arr[mid1] > arr[mid2]:
            right = mid2 - 1
        else:
            left = mid1
            right = mid2
    
    return left
 
result = ternary_search(arr)
print(f"The peak element is: {arr[result]} at index: {result}")
```
 
**Test cases passed:**
- `[1, 3, 7, 12, 18, 23, 19, 14, 8, 3]` → 23 at index 5 ✅
- `[3, 2, 1]` → 3 at index 0 ✅
- `[1, 5, 1]` → 5 at index 1 ✅
 
**Edge case pending (revisit mein):**
- `[1, 2, 3]` → 2 deta hai, 3 hona chahiye
- Root cause: Jab `m = 1` aur array 3 elements ka ho, mid1 == mid2 == middle index. Equal case mein middle element aur uske aage wala dono eliminate ho jaate hain.
 
---
 
## Key Learnings
 
**Sabse bada insight:** Ternary search sorted array mein binary search se **slower** hota hai. Steps kam hote hain (log₃n vs log₂n) lekin har step mein 2 comparisons lagte hain — total mein ~1.26x zyada comparisons.
 
**Mid formula ka evolution:**
- Attempt 1: `mid = (left+right)//2` — unnecessary
- Attempt 2-3: `(left+right)//3` — left ko base nahi banata, stuck ho jaata hai
- Final: `m = (right-left+1)//3`, `mid1 = left+m`, `mid2 = right-m` — correct
 
**Equal case ki understanding:**
- `mid1 == mid2` tab hota hai jab region bahut chhota ho
- Iss case mein peak sirf mid1 se mid2 ke beech possible hai
- `+1/-1` mat lagao — mid1 aur mid2 khud bhi valid candidates hain
 
**Index vs Value — baar baar aaya:**
- `left`, `right`, `mid1`, `mid2` — ye sab **indices** hain
- `arr[mid1]` — **value** hai
- Pointer update mein hamesha index assign karo, value nahi
 