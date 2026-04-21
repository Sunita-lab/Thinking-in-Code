#user ke hisab se array ke elements aur search karne wala element input lena hai
print("Enter the elements of the array: ")
arr = list(map(int, input().split()))
print("Enter the number to be searched: ")
x = int(input())

#soch : function bana leti hun ek, sbse pehle recursion man mein aaya
def binary_search(arr, x):
    n = len(arr)
    
    if arr[n//2] == x:
        return n//2
    elif arr[n//2] > x:
        return binary_search(arr[:n//2], x)
    else:
        return binary_search(arr[n//2 + 1:], x)

result = binary_search(arr, x)
print(f"Element found at index: {result}")
#time complexity is O(log n) because we are halving the search space in each step.
#space complexity is O(log n) in the average case due to recursive call stack, but in the worst case (if the element is not found), it can go up to O(n) if the array is not sorted and we end up checking all elements. However, for a sorted array, the space complexity would be O(log n) due to the recursive calls.
