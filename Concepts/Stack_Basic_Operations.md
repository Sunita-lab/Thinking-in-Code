# Stack — Basic Operations

## What is this concept — apne words mein
Stack ek data structure hai jisme sirf **upar se hi** cheez daal sakte ho aur **upar se hi** nikal sakte ho — LIFO (Last In First Out). Real life analogy: tiffin dabba stack — sबसे upar wala dabba hi pehle nikalta hai, sबसे upar hi naya dabba rakh sakte hain.

## Intuition — ye exist kyu karta hai
Jab bhi kisi problem mein **"sबसे recent chiz ko pehle handle karna hai"** wala pattern ho, wahan stack fit baithta hai. Jaise brackets match karna, undo/redo, function calls (call stack) — sab mein "abhi jo last add hua wahi pehle process hoga" wala logic hai.

## Core operations aur unka mapping
Python list ke through implement karte waqt:

| Operation | Kaam | List operation |
|---|---|---|
| push | element upar daalo | `list.append(x)` |
| pop | upar wala nikaalo | `list.pop()` |
| top/peek | upar wala dekho, hataao nahi | `list[-1]` |
| isEmpty | khali hai ya nahi check karo | `not stack` |
| size | kitne elements hain | `len(stack)` |

## Kaise samjha maine — journey
Shuru mein confusion tha ki "implement karna" ka matlab kya hota hai — jab concept (LIFO) clear tha, lekin "isko code mein kaise dhaalna hai" samajh nahi aa raha tha. Realization ye hui ki implementation ka matlab hai — abstract concept (push/pop/top) ko kisi **actual data structure ke available operations** mein translate karna. Array/list ke case mein, Python ki list ke built-in methods (append, pop) already yehi kaam karte hain, isliye mapping seedha ho gaya.

## Maine kya galti ki thi samajhte waqt
- `stack = []` ko class ke andar likha tha lekin `__init__` ke **bahar** — isse wo **class attribute** ban gaya, instance attribute nahi. Iska result: saare objects ek hi list **share** karte hain, jabki har object ko apni **alag, fresh** list chahiye thi.
- Isse pehle `__init__`/constructor ka role hi clear nahi tha — samjha ki C++ ke constructor jaisa hi role hai, jo har naye object banne par automatically chalta hai aur us specific object ke liye fresh setup karta hai.
- Fix: `self.stack = []` ko `__init__` ke **andar** likhna — taaki har naya object banne par Python `__init__` chalaye aur naya, alag list mile.

## Connection — amortized complexity
List-based push mostly O(1) hota hai, lekin jab list ki internal capacity full ho jaati hai aur Python resize karta hai (naya bada array banake sab copy karta hai), tab wo particular push O(n) ho jata hai. Overall average O(1) hi rehta hai — isko **amortized O(1)** kehte hain.