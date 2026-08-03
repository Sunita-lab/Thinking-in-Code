# Problem: BST Insert (GFG) — also covers LC 701 (Insert into a BST)

*LC 701 solved right after this — same problem, same approach, no separate note needed.*

## Problem explanation
Given root of a BST aur ek key, key ko BST mein us jagah insert karna hai jahan BST property maintain rahe. Return updated root.

## Session journey (how this was derived)
Session ek library/phone-directory analogy se shuru hui — insert karna tha "Manav" ko ek naam-based tree mein (Rohan root, Kabir uska left child).

- Pehla instinct galat tha: socha gaya insertion "left to right fill karo, jahan bhi tree incomplete/khaali ho" — yani heap-style level order insertion. Ye normal BT/heap ke mental model se aaya tha.
- Directory analogy ne isse break kiya: Manav ko daalne ke liye alphabetically compare kiya gaya — Rohan se pehle → left, phir Kabir se baad mein → right, phir khaali mila → wahan insert. Isse realize hua ki position **decided** hoti hai comparison se, random slot nahi.
- Isi se BST property khud derive hui: left mein sab chhote, right mein sab bade — har node ke liye.
- Phir socha gaya ki ye process recursive hai ya iterative. Pehla jawab galat tha — "recursive kyunki left subtree pura traverse karna padega phir root phir right" — ye actually inorder traversal ka reasoning tha, insertion ka nahi. Correction: insertion mein sirf **ek direction** mein neeche jaate hain, har step pe ek comparison, poora subtree traverse nahi karte.
- Base case discover kiya: jab current position `None` mile, wahi naya node insert hota hai.
- Recursive stitching ka concept aaya: `node.right = insert(node.right, value)` — return value ko wapas parent ke pointer mein assign karna zaroori hai warna naya node tree se disconnect reh jaata (floating node).

## Approach used
Recursive insertion:
1. Base case: agar `root` is `None` → naya `Node(key)` banao, return karo
2. Agar `key < root.data` → `root.left = insert(root.left, key)`
3. Agar `key > root.data` → `root.right = insert(root.right, key)`
4. `return root`

## Attempts and fixes

**Attempt 1 (bug):**
```python
def insert(self, root, key):
    current = root
    if not current:
        return Node(key)
    if key < current.data:
        current.left = self.insert(current.left, key)
    if key > current.data:
        current.right = self.insert(current.right, key)
    # missing return here!
```
Bug: function ke end mein koi explicit `return` nahi tha. Dono `if` conditions ke false hone ya un blocks ke execute hone ke baad, function implicitly `None` return kar raha tha — jo upar wale recursive call mein `node.left`/`node.right` ko `None` se overwrite kar deta.
Root cause: har `if` block ke andar action ho raha tha, lekin function ke overall return statement ko bhool gaye likhna — recursive functions mein "har path se kuch return ho raha hai" check karna zaroori hai.

**Fix:** `return root` add kiya function ke end mein.

**Follow-up question discuss hui:** `current = root` likhna zaroori tha kya? Answer: nahi — `current` sirf ek reference/alias tha, `root.left = insert(...)` seedha bhi utna hi correct chalta. Dono same object ko point karte hain, isliye `current.left = ...` karne se `root` khud bhi update ho gaya (mutation same object pe).

**Duplicate handling discuss hua:** Agar `key == current.data` toh kya karein — ye ek design choice hai (left treat karo, right treat karo, ya insert hi mat karo). Is problem mein specifically nahi decide kiya gaya (koi duplicate test case nahi aaya abhi), lekin note kar liya ki search logic ke saath consistent hona chahiye jo bhi decision liya jaaye.

## Key learning
Sabse bada insight: BST guarantee ki wajah se sirf **current node se compare karke** pura ek subtree prune ho jaata hai — deeper nodes (jaise `root.left.val`) ko directly check karne ki zaroorat nahi padti. Yahi property hai jo BST operations ko average case O(log n) banati hai, poori O(n) linear scan nahi lagti.

Doosra insight: insertion recursive hai lekin traversal jaisa nahi — sirf ek path follow hota hai (left ya right), poora subtree explore nahi hota. Recursive call ka return value wapas parent ke pointer (`.left`/`.right`) mein assign karna zaroori hai, warna naya node tree se disconnect reh jaata hai.