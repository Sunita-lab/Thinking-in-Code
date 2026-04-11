#user se uske man mutaabik array ke elements aur search karne wala element input lena hai
print("Enter the elements of the array: ")
arr = list(map(int, input().split()))
print("Enter the number to be searched: ")
x = int(input())

#foundat array isliye hai ki agar multiple occurrences hai to sabko ek sath print karenge bina ki har ek occurrence ke liye alag alag print karna pade.
#edge case alert: multiple occurrences bhi ho skte hai
foundat = []

#edge case alert: agar array empty hai to us case me loop chalane ki zarurat nahi hai, directly print kar do ki array empty hai.
if len(arr) != 0:
    for i in range(len(arr)):
        if arr[i] == x:
            foundat.append(i)
            # element milta hai to sidhe print nhi kar rhe store karke baad mein print krenge
    
    if foundat:
    #learning alert: if foundat bhi likh skte hai mtlb agar foundat empty hai to value False hai uska    
        print("Element found at indices: ", foundat)
    else:
        print("Element not found in the array") 
    ## agar foundat empty hai to loop pura chala lekin koi match nahi mila
   # note: foundat list space complexity badhati hai O(k) tak, lekin loop completion track karne ka sabse clean tarika yahi hai all-occurrences case mein
   # general doubt: loop chala ki nahi jaanne ke liye har case mein alag approach lagti hai — flag, list, counter, ya break — koi universal syntax nahi      
    #just thought: agar aisa koi direct syntax hota ki ye pata chal jaaye ki loop chal gaya lekin uske andar ka kuch kaam nhi hua hai to mujhe if foundat nhi likhni padti na?     
else:
    print("Array is empty")

#Time complexity for worst case is O(n) because we have to check each element of the array once.
#  In the best case, if the element is found at the first position, the time complexity is O(1). 
# In the average case, the time complexity is O(n) because we may have to check half of the elements in the array before finding the element or determining that it is not present.  
# Space complexity is O(k) where k is the number of occurrences of the element in the array, because we are storing the indices of the found elements in a list.
#  In the worst case, if all elements are the same and equal to x, then space complexity would be O(n). 