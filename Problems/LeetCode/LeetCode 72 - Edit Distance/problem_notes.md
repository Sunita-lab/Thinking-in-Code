# Problem: Edit Distance
**GFG:** Edit Distance | **LeetCode:** 72 (Edit Distance) — same problem, combined note.

## Problem statement (in short)
Do strings diye hain — ek source, ek target. Minimum operations (insert, delete, replace) chahiye source ko target mein convert karne ke liye.

## Derivation journey

**Pehla connection (khud banaya, LCS se):**
"L2 ko L1 banane ke liye L1 kितna already L2 mein bacha hai wo dekhna hoga (LCS). Agar LCS = len(L1), toh sirf extra L2 characters delete karne honge."

**Test 1 (khud diya) — sirf insert/delete wala case:**
`L1="ABC"`, `L2="AXBYC"` — LCS=3=len(L1). Formula: `len(L2)-LCS = 5-3 = 2` deletions. **Match kiya.**

**Test 2 — ulta case:**
`L1="ABC"`, `L2="AC"` — LCS=2=len(L2). Formula: `len(L1)-LCS = 3-2 = 1` insertion. **Match kiya.**

**Test 3 — mix case, formula break hua:**
`L1="ABC"`, `L2="AXC"` — LCS=2. Pure formula se 2 operations (1 delete X + 1 insert B). Lekin manually socha: **replace** X ko B se seedha kar do — **1 operation** mein kaam ho gaya. Yahin se clear hua ki jab replace allowed ho, pure-LCS approach **suboptimal** hai — teeno operations ko explicit recurrence mein sochna zaroori hai.

**Recurrence derivation:**
- `f(i,j)` = min operations to convert `source[j...]` into `target[i...]` (suffix-based, jaisa LCS mein tha)
- **Match:** `f(i,j) = f(i+1,j+1)`, no cost
- **Mismatch — teeno options, min lo, +1 cost:**
  - Confusion aayi initially ki subproblems ka `(i',j')` decide karna — resolve hua **concrete character-by-character trace** se (`s1="AB"`, `s2="CB"`):
    - **Replace** `s2[j]→s1[i]`: dono position "handled," dono pointer aage → `f(i+1,j+1)`
    - **Delete** `s2[j]`: source ka character consume hua, target ka abhi baaki → `f(i,j+1)`
    - **Insert** target ke liye source mein: target ka character "matched," source ka original abhi wahin khada → `f(i+1,j)`
  - Sab teeno derive khud kiye gaye, ek ek karke trace ke through confirm hue

**Base cases — thodi galti hui, self-corrected:**
- Base case values (`len(L2)-j` deletions, `len(L1)-i` insertions) khud sahi bataye
- **Implementation mein bug aaya:** `if/elif` se `i==len(s1)` aur `j==len(s2)` check kiya bina explicit "dono ek saath" condition ke. Doubt uठaya: "agar dono ek saath sahi ho jaayein, elif se doosra skip ho jaayega, galat answer aayega?" — Ye **valid reasoning thi**. Isके baad dono ko `if` kiya (dono independently check), wo bhi galat nikla kyunki corner cell ka answer sirf `0` hona chahiye, kuch aur nahi. Phir match-wale ko `if` kiya toh index error aaya, wahan se samjha ki structure `if/elif/elif/else` chahiye poore chain ke liye, saath mein ek explicit `if i==len(s1) and j==len(s2): pass` (table already 0 se init hai, wahi sahi value hai corner ke liye) sबसे pehle.
- **Nuance jo baad mein samne aayi:** turns out arithmetic khud hi corner case ko self-cancel kar deta (`len(s2)-j` jab `j=len(s2)` ho toh khud `0` ban jaata), isliye bina explicit `and` check ke bhi GFG pass ho gaya tha. Lekin doubt **sahi tha** puchna — sirf is specific formula mein coincidentally bug nahi bana. Explicit `and` check zyada readable/defensive hai, rakhna sahi.

## Attempts & Final Code

**Attempt 1 — match case mein extra `+1` ki galti:**
```python
elif s1[i] == s2[j]:
    dp[i][j] = dp[i+1][j+1] + 1   # galat — match mein cost nahi honi chahiye
```
Khud pakda aur fix kiya — match hone par koi operation ki zaroorat nahi.

**Attempt 2 — corner case ke liye if/elif ka structuring confusion (upar detail mein describe kiya gaya)**

**Final correct code:**
```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        rows = len(word1)+1
        cols = len(word2)+1
        dp = [[0]*(cols) for _ in range (rows)]
        for i in range (rows-1,-1,-1):
            for j in range (cols-1,-1,-1):
                if i == len(word1) and j == len(word2):
                    pass
                elif i == len(word1):
                    dp[i][j] = len(word2) - j
                elif j == len(word2):
                    dp[i][j] = len(word1) - i
                elif word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(dp[i+1][j+1], dp[i+1][j], dp[i][j+1]) + 1
        return dp[0][0]
```

Note: loop range yahan `rows-1` se start hota hai (LCS ke `rows-2` se different) — kyunki last row/column pre-filled nahi hain, unhe bhi isी loop ke andar `if/elif` se handle kiya ja raha hai.

## Mid-way doubts (aur kaise solve huye)

1. **"Insert/delete/replace ke liye subproblem `(i',j')` kaise decide hue?"** — Concrete character trace se resolve hua (`s1="AB"`, `s2="CB"` example), ek ek operation dhyan se socha gaya: jiska character "handle" ho gaya uska pointer aage, jiska baaki hai wo wahin.

2. **"Corner case (dono ek saath khatam) ke liye if/elif sahi hai ya nahi?"** — Genuine valid doubt tha. Iterative debugging se resolve hua:
   - Pehla version: sirf `if/elif` (`i==len(word1)` phir `elif j==len(word2)`), koi explicit `and` check nahi. Doubt uठाया: agar dono ek saath true hon, `elif` doosra check hi nahi karega, kya galat answer aayega?
   - Turns out — **nahi**, is specific case mein galat nahi aata, kyunki jab dono condition ek saath true hoti hain, pehla wala formula (`len(word2)-j`) khud `0` ban jaata hai (kyunki `j` bhi `len(word2)` ke barabar hai us waqt) — **self-cancelling coincidence**.
   - Phir bhi, doosra galat attempt kiya gaya: dono ko independent `if` (na ki `elif`) bana diya — ye galat nikla, kyunki dono conditions ek saath true hone par **dono branches overwrite** kar sakte the ek dusre ko, jo bug ban sakta tha.
   - Phir match-wale ko bhi `if` (elif ki jagah) kiya toh **index error** aaya — samjha gaya ki poori chain `if/elif/elif/else` honi chahiye (mutually exclusive branches), na ki independent `if`s.
   - Final version mein **explicit `if i==len(word1) and j==len(word2): pass`** rakha gaya — sबसे pehle, corner case ko explicitly, clearly handle karte hue (table already `0` se init hai, wahi sahi value hai). Ye zaroori nahi tha (coincidental self-cancellation ke wajah se) but **behtar practice hai** — readability aur future-robustness dono ke liye (agar kabhi base-case formulas is tarah self-cancel na karein kisi variant mein, explicit check bug turant pakad legi).

3. **"Ye pura process kितna abstract lag raha hai — actual insert/delete/replace toh ho hi nahi raha, sirf socha jaa raha hai."** — Ye khud ek insight tha jo doubt ki tarah aaya: recognize kiya ki ye "illusion of modification" hai — length kabhi actually change nahi hoti, sirf hypothetical costing chal rahi hai. Aur khud identify kiya ki isliye ye "queue jaisa," systematic tareeke se kaam karta hai kyunki changes hamesha ek consistent direction (start se end) mein propagate ho rahe hain.

4. **Sबसे deep doubt — fill order vs movement direction:** "hum kisi step par indices mein peeche nahi ja rahe, phir bhi table last se kyun fill kiya?" Ye do alag concepts the jo mix ho rahe the — **call/movement direction** (forward, `i,j` badhते hain) vs **value-dependency direction** (reverse — `f(0,0)` depend karta hai bade `i,j` walo par, base case sबसे pehle "known" hote hain). Recursion call-tree se concrete trace dikhaya gaya jahan calls forward jaati hain but return-values reverse order mein milte hain. Khud crisp summary di: "ek call apna kaam tab tak nahi kar sakti jab tak agli (forward) call apna kaam na kar de — dependency forward hai," isliye fill bhi dependency ke hisaab se hona chahiye (chhote-dependency/base-case cells pehle).

   **Final, sबसे precise reformulation (khud, standalone insight ke roop mein, baad mein diya):** "**Table filling direction actually recursion ke returning ka direction hai.**" Recursion **calls** forward jaati hai (`i,j` badhते), lekin **values return** reverse order mein hote hain (base case se `f(0,0)` tak bubble karte hue). DP tabulation jab bottom-se-top fill karta hai, wo bas is "return path" ko explicitly, bina call-stack ke, loops se replicate kar raha hota hai. Ye ek generalizable rule ban gaya: kisi bhi naye suffix-based 2D DP mein fill-order confuse ho toh — socho recursion mein values kis order mein "return" honge (base case se upar), wahi order table-fill ka bhi hoga.

5. **DAG-safety observation (khud noticed, side insight):** har operation mein `i,j` sirf badhते hain kabhi ghatate nahi, isliye recursion kabhi cycle mein nahi phasti — clean DAG structure.

## Syntax / Python concepts touched
- `if/elif/elif/else` chain — jab multiple mutually-relevant conditions hon jisme se sahi ek chunna zaroori ho (khaaske corner cases mein), tab explicit ordering aur `pass` ka use.
- Reused nested list comprehension pattern for 2D table init (LCS se continue).

## Key insight (apne words mein)

"Yahan koi actual insert, delete, ya replace ho hi nahi raha hai. Replace ke case mein intuitively samajh aata hai, baaki dono (insert/delete) thode abstract lagte hain kyunki length change nahi ho rahi — bas socha jaa raha hai ki 'aise agar hota to kya hota.' Ye illusion of modification isliye kaam karta hai kyunki saare changes ek queue jaise tarike se, shuru se end ki taraf ho rahe hain — koi bhi teeno operations mein se kuch bhi karo, hamesha shuru wale end se match hota jaata hai, isliye recursion/DP kabhi peeche nahi jaati aur loop safe chalti hai (DAG structure)."