# Ternary Search
 
## Apne words mein — ye kya hai
 
Binary search sorted array mein kaam karta tha — ek direction mein bada, doosre mein chhota. Ternary search ek alag property pe kaam karta hai — **unimodal function.** Matlab pehle badhta hai, ek peak aata hai, phir ghatta hai. Target pata nahi hota — peak dhundha jaata hai.
 
## Intuition — ye kyun exist karta hai
 
Binary search ka ek strict requirement tha — sorted array. Lekin agar array sorted nahi hai, sirf hill shape ka hai (unimodal) — toh binary search ka left/right logic kaam nahi karta. Ternary search usi gap ke liye hai.
 
## Unimodal Function kya hai
 
```
1, 3, 7, 12, 18, 23, 19, 14, 8, 3
             ↑ pehle badhta hai    ↑ phir ghatta hai
                         ↑ peak
```
 
Ek hi peak hota hai. Do peaks ho toh ternary search kaam nahi karta.
 
## Core Logic — mid1 vs mid2
 
Array mein do markers lagate hain — mid1 aur mid2. Inhe aapas mein compare karte hain (target se nahi — kyunki target/peak ki value pata hi nahi hoti pehle se).
 
```
mid1 = left + (right - left + 1) // 3
mid2 = right - (right - left + 1) // 3
```
 
**Teen cases:**
 
| Condition | Matlab | Action |
|-----------|--------|--------|
| arr[mid2] > arr[mid1] | Peak mid1 ke left mein nahi ho sakta | left = mid1 + 1 |
| arr[mid1] > arr[mid2] | Peak mid2 ke right mein nahi ho sakta | right = mid2 - 1 |
| arr[mid1] == arr[mid2] | Peak sirf beech mein ho sakta hai | left = mid1, right = mid2 |
 
## Binary Search se comparison
 
| | Binary Search | Ternary Search |
|--|---------------|----------------|
| Kab use karein | Sorted array, target pata ho | Unimodal array, peak dhundna ho |
| Steps | log₂(n) | log₃(n) |
| Comparisons per step | 1 | 2 |
| Total comparisons | log₂(n) | ~1.26 × log₂(n) |
| Sorted array mein | Faster | Slower |
 
**Counterintuitive insight:** Ternary search sorted array mein binary se slower hai — 3 parts karne se steps kam hote hain lekin har step mein 2 comparisons lagte hain. Dono milake total zyada ho jaata hai.
 
## Time & Space Complexity
 
| | Complexity |
|--|------------|
| Time | O(log₃ n) |
| Space (iterative) | O(1) |
| Space (recursive) | O(log₃ n) call stack |
 
## Implementation (Iterative)
 
```python
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
    
    return left  # index of peak
```
 
## Gaps / Revisit mein dekhna
 
- Small array edge case — jab `m = 1` aur `mid1 == mid2` ho jaate hain, equal case mein peak bahar reh sakta hai
- Valley (minimum) dhundne ke liye conditions ulti ho jaayengi — try karna revisit mein
- Unimodal function mein specific value dhundna (sirf peak nahi) — explore karna hai
 
## Kahan kaam aata hai
 
- Mathematical optimization — unimodal cost functions mein minimum/maximum dhundna
- Competitive programming — peak element, bitonic array problems
- Real world — signal processing mein peak frequency dhundna