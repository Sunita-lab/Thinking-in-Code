# Valid Parentheses — Concept

## What is this concept — apne words mein
Diya hua string sirf brackets (`(`, `)`, `{`, `}`, `[`, `]`) ka bana hota hai. Check karna hai ki har opening bracket ka **sही matching closing bracket** sही order mein aaya hai ki nahi — matlab brackets properly "nested/balanced" hain ya nahi.

## Intuition — stack kyu use hota hai
Sबसे pehle socha tha — "leftmost aur rightmost ko ek saath match karo, andar aate jao." Ye approach test kiya `()[]` pe — leftmost `(`, rightmost `]` — ye seedha match nahi karte, jabki string actually valid hai. **Ye approach yahi break ho gaya** — realization hui ki bracket ka "partner" uske physical position (left/right end) se decide nahi hota, balki **kis order mein khula tha** usse decide hota hai.

Sahi intuition: jab bhi ek closing bracket aata hai, usko **sबसे recent unclosed opening bracket** ke saath match karna hota hai — na ki sबसे pehle wale se. "Sबसे recent pehle handle hoga" — yahi LIFO hai, isliye **stack** fit baithta hai.

## Algorithm (khud derive kiya)
1. String ko left se right traverse karo
2. **Opening bracket** mile → push karo stack mein
3. **Closing bracket** mile:
   - Stack khali hai → invalid seedha (kisi ko match karne ke liye nahi hai)
   - Stack khali nahi hai → top pop karo, check karo ki wo iska matching opening bracket hai ki nahi. Match nahi hua → invalid
4. Poori string process hone ke baad — stack **empty** hai → valid; kuch bacha hai (unclosed openings) → invalid

## Edge cases jo socha
- `(]` — top match nahi karta → invalid
- `)( ` — closing bracket aaya lekin stack khali hai (pehla character hi closing hai) → seedha invalid, push karne ka koi matlab nahi
- Sirf openings bache reh jayein end tak (jaise `"["`) → stack empty nahi hoga end mein → invalid

## Implementation ka core tool
Matching pairs track karne ke liye **dictionary** use hoti hai — `{closing: opening}` mapping. Reverse lookup (value se key dhundhna) dict mein direct/efficient nahi hota (O(n)), isliye mapping ko **closing → opening** direction mein rakhna better hai (O(1) lookup).