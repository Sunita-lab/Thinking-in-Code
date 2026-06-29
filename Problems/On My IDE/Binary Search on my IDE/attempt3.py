#user ke hisab se array ke elements aur search karne wala element input lena hai
print("Enter the elements of the array: ")
arr = list(map(int, input().split()))
print("Enter the number to be searched: ")
x = int(input())

#is baar recursion nhi, iterative approach try karte hain
def binary_search(arr, x): 
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            right = mid - 1
        else:
            left = mid + 1
            
    return -1  # Element not found
result = binary_search(arr, x)
if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the array.")
#time complexity is O(log n) because we are halving the search space in each step
#space complexity is O(1) because we are using only a constant amount of extra space for the left, right, and mid variables.