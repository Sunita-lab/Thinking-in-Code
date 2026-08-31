# Problem: Longest Common Subsequence
**GFG:** LCS | **LeetCode:** 1143 (Longest Common Subsequence) — same problem, combined note.

## Problem statement (in short)
Do strings/sequences diye hain, sabse lambi common subsequence ki length nikalo — order maintain karte hue, skip allowed.

## Derivation journey (poori conversation ka flow)

**Scenario:** Do movie-watching history lists — apni aur best friend ki. Sawaal: order maintain karte hue overlap kितna hai.

**Attempt 1 (galat) — char by char / index by index matching:**
`L1[i]` ko `L2[i]` se compare karna (same index). Turant break hua — real example (`Inception, Interstellar, Dunkirk, Tenet, Oppenheimer` vs `Interstellar, Dunkirk, Barbie, Tenet`) mein index 0 pe hi mismatch aaya, jabki visually common movies clearly maujood thi.

**Attempt 2 (galat) — greedy pair matching, i fix karke j scan karo, pehla match le lo:**
Chhote example mein kaam kar gaya, but tricky example pe break hua:
`L1 = Amelie, Gravity, Gravity, Tenet, Amelie, Barbie`
`L2 = Gravity, Xmen, Tenet, Xmen, Amelie, Yesterday, Barbie`
Is approach ne sirf `ans=1` diya. Wajah: L1[0]=Amelie ko greedily L2[4]=Amelie se match kar diya (pehla jo mila), jo list mein bahut aage tha — isse Gravity aur Tenet jaise better, pehle-wale matches "use ho gaye" is decision ki wajah se aur miss ho gaye.

**Manual check:** Actual LCS nikla `Gravity → Tenet → Amelie → Barbie` = length **4**. Yahin se **subsequence ki sahi definition** (relative order, skip allowed, no adjacency needed) clear hui — jo pehle "strictly next hi aana chahiye" jaisa assume kiya ja raha tha.

**Brute force socha:** Saare possible ordered subsets dono lists ke generate karo, jo match karein unme se max length lo. (Exponential — 2^n subsequences per string — isliye optimize karna zaroori.)

**Recurrence derivation (guided):**
- Do pointers `i, j` — `f(i,j)` = LCS of L1[i...] aur L2[j...] (suffix-based, prefix nahi)
- **Match case:** hamesha include karo. Ye kyun safe hai — chhote test cases se verify kiya (`L1="A,B,A"`, `L2="A,A,B"` par match turant lene se LCS=2, skip karne se sirf 1)
- **No-match case:** dono options try karo — `L1[i]` skip ya `L2[j]` skip — max lo. **Dono ko saath skip nahi karte** kyunki wapas "same index" wali galti ban jaati (flexibility khatam)
- **Base case:** `i == len(L1)` ya `j == len(L2)` → return 0. Pehle `-1` ki galti hui thi is derivation mein, khud correct kiya (test karke socha: `i=2` valid hai length-3 array mein, `i=3` invalid — toh `len(L1)` hi sahi termination hai, `-1` nahi)

**Table conversion:** Size `(len(L1)+1) × (len(L2)+1)`, saari `0` se initialize (base case auto-cover), fill order bottom-to-top / right-to-left (bade i,j pehle, kyunki chhote i,j unhi par depend karte hain).

## Attempts & Final Code

**Sirf ek attempt lagi — pehli hi baar mein sahi (5 minutes mein likha):**

```python
class Solution:
    def lcs(self, s1, s2):
        rows = len(s1)+1
        cols = len(s2)+1
        dp = [[0]* (cols) for _ in range (rows)]
        for i in range (rows-2, -1, -1):
            for j in range (cols-2,-1,-1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                if s1[i] != s2[j]:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]
```

**Ek chhoti si implementation slip (turant self-corrected):** loop range pehle `rows-1` likha tha, error aaya, samajhke `rows-2` kiya (kyunki last valid index `rows-1` hi hoti, aur wo already base-case row hai jo `0` se filled hai — traversal ko `rows-2` se shuru karna tha, ek row pehle se).

**Style note (bug nahi):** `if/if` use kiya match aur no-match ke liye, `if/elif` cleaner hota (dono conditions mutually exclusive hain, toh functionally sahi hai).

## Mid-way doubts (aur kaise solve huye)

1. **"Subsequence ka matlab relative order hai, strictly agla hi aana chahiye aisa nahi?"** — Confirm hua ki haan, relative order zaroori hai but adjacency nahi. Substring se explicit contrast karke clear hua.

2. **"Jab match nahi hota, i+1,j aur i,j+1 same answer kyun nahi de rahe? Mera dimaag isse normal nested-loop traversal (i fix, j pura iterate, phir i badhao) se jodne ki koshish kar raha hai."** — Ye sabse deep doubt tha. Resolve hua concrete counter-example se (`L1="XAB"`, `L2="AB"` → `f(1,0)=2` but `f(0,1)=1`), aur distinction clear hui: **traversal order** (kis sequence mein table fill karo) aur **recurrence** (ek cell ki value kaunse doosre specific cells se aati hai) do alag concerns hain. `f(i+1,j)` aur `f(i,j+1)` genuinely do different subproblems hain — same aana koi guarantee nahi.

3. **Related misconception jo isi doubt se nikli:** "agar L1 se ek element hata do aur poori L2 available hai, toh LCS = len(L2) ho jaayega." Galat — LCS hamesha dono strings se chhota ya barabar hota hai. Test kiya `L1="AB"`, `L2="BA"` se — dono `f(1,0)` aur `f(0,1)` alag values (aur dono `len(L2)` se kam) de rahe the.

4. **"Agar match hone par turant le liya, kya aage koi lambi possibility miss ho sakti hai?"** — Test kiya `L1="A,B,A"` vs `L2="A,A,B"` se — match turant lena hamesha ≥ skip karna nikla, kabhi kam nahi.

5. **Extension doubts (dono khud puche, dono sahi socha):**
   - "Agar dono strings same length hon, toh kya i+1,j ya i,j+1 kuch bhi lene se chalta?" — Nahi, khud correct kiya apni pichli galti pakadke (LCS chhota ho sakta hai target string se, lambi nahi)
   - "Agar ye problem substring (strict continuity) hoti, toh bhi yahi DP chalta?" — Khud sahi socha: match par chain continue but no-match par **reset to 0** (skip-branches ka max() nahi), aur ek global max variable track karna padega kyunki best substring beech mein kahin bhi khatam ho sakti hai.

## Syntax / Python concepts touched

- Nested list comprehension for 2D table init: `[[0]*(cols) for _ in range(rows)]` — row-wise fresh lists banata hai (mutable default trap se bachne ka sahi tareeka, `[[0]*cols]*rows` nahi likha jo shared-reference bug deta)
- `range(rows-2, -1, -1)` — reverse iteration syntax, stop `-1` isliye taaki `0` bhi included ho

## Key insight (apne words mein)

"Subsequence ki galat framing thi — mera dimaag sirf ek step aage dekhne ki freedom de raha tha (greedy, pehla match pakdo), jabki asli problem mein dono directions (i skip ya j skip) explore karna padta hai kyunki pata nahi kaunsa better hoga. Aur jab match milta hai, wahan koi choice nahi — hamesha lena hai, kyunki wo kabhi loss nahi karwata."