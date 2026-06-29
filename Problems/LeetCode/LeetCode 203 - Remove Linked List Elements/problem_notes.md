# LC 203 — Remove Linked List Elements
## Attempt 1

## Approach
- self.head use kiya — apni LinkedList class ka pattern LeetCode pe apply kar diya
- Head aur non-head nodes ke liye alag alag conditions likhi
- prev pointer ka concept nahi aaya — directly current node pe kaam karne ki koshish ki

## Kya galat hua
- LeetCode mein self.head nahi hota — head parameter seedha milta hai
- self.head use karne se NameError aata — code run hi nahi hota
- Head ka special case alag handle kiya — unnecessarily complex ho gaya
- current.next.next directly set kiya bina prev track kiye — logic unsound tha

## Logic kitni sahi thi
- Sahi tha: val match hone pe node skip karna chahiye — direction sahi thi
- Galat tha: LeetCode ka context samajh nahi aaya — apni class ka pattern apply kar diya

## Complexity
- Time: O(n) intent tha — lekin code run nahi hota
- Space: O(1)



## Attempt 2

## Approach
- Dummy node technique — ek fake node banaya head se pehle
- dummy.next = head — ab head ka special case automatically handle
- current = dummy se traverse shuru
- current.next.val == val — skip karo, warna current aage badho
- return dummy.next — hamesha sahi head milega

## Kya achha tha
- Dummy node khud se socha — hint se samjha aur implement kiya
- dummy.next return karna — reliable approach
- Code clean aur readable tha

## Kya galat hua pehle
- head variable manually update karne ki koshish ki — unreliable tha
- else mein current.next = current.next.next likha — current move nahi ho raha tha, next skip ho raha tha

## Key learning
- Dummy node — jab bhi head delete hone ka chance ho, dummy use karo
- current move karo, next nahi — traverse mein current = current.next
- dummy.next hamesha reliable — head variable manually track karna error prone hai

## Complexity
- Time: O(n) — ek baar traverse
- Space: O(1) — dummy ek extra node hai, O(1) hi maana jaata hai