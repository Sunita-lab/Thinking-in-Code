# DLL — Insert and Delete at Position

## What was built
- DLL Node class — prev + data + next
- Insert at given position
- Delete at given position

## Key learnings
- 4 pointers set karne padte hain insert mein — order matter karta hai
- current.next ka reference pehle save karo, phir current.next move karo
- Delete mein sirf 2 pointers — prev.next aur next.prev

## Edge cases jo dhyan rakhne hain
- Position 0 — head.prev = None karna zaroori
- Last position insert — current.next None hai, uska prev set karne ki zaroorat nahi
- Last position delete — current.next None hai, check lagana padega