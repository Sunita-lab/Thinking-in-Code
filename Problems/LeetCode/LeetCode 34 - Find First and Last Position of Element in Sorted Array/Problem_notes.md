# LC 34 — Find First and Last Position of Element in Sorted Array
### Problem Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

**Attempt status:** Attempt 1 ✅ | Attempt 2 ✅  
**Date:** 2025-05-10 

---

## Problem

Given a sorted array of integers and a target value, return the first and last position of the target. If not found, return `[-1, -1]`.

---

## Attempt 1 — Brute Force (O(n)) - (88/88 Passed)

### Approach
Binary search se target find kiya. Jab `nums[mid] == target` mila — wahan se **linear scan** left aur right dono taraf chalayi first aur last occurrence dhundne ke liye.

### Code
```python
class Solution(object):
    def searchRange(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                left1 = mid
                right1 = mid
                for i in range(mid-1, -1, -1):
                    if nums[i] == target:
                        left1 -= 1
                    else:
                        break
                for i in range(mid+1, len(nums)):
                    if nums[i] == target:
                        right1 += 1
                    else:
                        break
                return [left1, right1]
        return [-1, -1]
```

### Time Complexity
**O(n)** — Binary search O(log n) tha, par linear scan worst case mein poora array traverse kar sakti thi (jaise saare elements same hon). O(log n) + O(n) = O(n) dominates.

### Gaps identified
- Binary search ka advantage kho gaya linear scan se
- Intuition sahi thi ki binary search se hi first/last dhundha ja sakta hai — par implement nahi ki thi

---

## Attempt 2 — Optimized (O(log n)) - (88/88 Passed)
### Link: https://leetcode.com/submissions/detail/1999665456/

### Approach
3 binary searches — pehle target dhundha, phir uske left half mein first occurrence, right half mein last occurrence.

**First occurrence logic:** `nums[mid] == target` milne pe seedha return nahi karna — `temp = mid` save karo aur `right = mid - 1` karke aur left jaao. Agar left mein kuch nahi mila toh `temp` hi answer.

**Last occurrence logic:** Same — `temp = mid` save karo aur `left = mid + 1` karke aur right jaao.

### Code
```python
class Solution(object):
    def searchRange(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                left1, right1, left2, right2 = 0, mid, mid, len(nums)-1
                while left1 <= right1:
                    mid1 = left1 + (right1 - left1)//2
                    if nums[mid1] != target:
                        left1 = mid1 + 1
                    else:
                        right1 = mid1 - 1
                while left2 <= right2:
                    mid2 = left2 + (right2 - left2)//2
                    if nums[mid2] != target:
                        right2 = mid2 - 1
                    else:
                        left2 = mid2 + 1
                return [left1, right2]
        return [-1, -1]
```

### Time Complexity
**O(log n)** — Teen binary searches, har ek O(log n).

### Reasoning defended
- `find_first` mein `nums[mid1] > target` possible nahi — kyunki `right1 = mid` se shuru kiya tha aur array sorted hai, toh left half mein target se bada element nahi hoga. Yeh observation khud kiya — sahi tha.
- Same logic `find_last` ke liye — `nums[mid2] < target` possible nahi kyunki `left2 = mid` se shuru kiya.

---

## Key Learnings

**1. Binary search ka advantage preserve karo**  
Agar binary search use kar rahe ho toh poori solution O(log n) rehni chahiye. Beech mein linear scan lagana matlab binary search ka point kho dena.

**2. "Target mila = return" nahi hota har baar**  
First/last occurrence ke liye target milne pe rukna galat hai — wahan se aur search karna padta hai us direction mein. `temp` save karna yahi kaam karta hai.

**3. Boundary reasoning important hai**  
`find_first` mein `right1 = mid` set kiya — isliye left half mein target se bada element aa hi nahi sakta. Yeh silently correct tha — Attempt 3 mein consciously design karna.

**4. Outer binary search redundant tha**  
Teen binary searches ki jagah do clean functions — `find_first` aur `find_last` — kaafi hain. Outer wala hatana next attempt ka kaam.

---

## What to do in Attempt 3 (Reconstruction)

- Notes mat dekho
- Seedha do clean functions likho — `find_first(nums, target)` aur `find_last(nums, target)`
- `searchRange` sirf dono ko call kare
- Boundary reasoning consciously socho — kyun `nums[mid] > target` ya `< target` possible nahi hota inner loops mein

---

## Pattern Family

Binary Search — **First/Last Occurrence variant**  
Related problems: Lower Bound, Upper Bound, Search Insert Position (LC 35)