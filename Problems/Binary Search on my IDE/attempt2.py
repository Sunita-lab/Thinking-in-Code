#user ke hisab se array ke elements aur search karne wala element input lena hai
print("Enter the elements of the array: ")
arr = list(map(int, input().split()))
print("Enter the number to be searched: ")
x = int(input())
#kuch baatein pata chali attempt1 se, usko use kiya hai
def binary_search(arr, x, left, right):
    if left > right:
        return -1  # Element not found

    mid = left + (right - left) // 2

    if arr[mid] == x:
        return mid
    elif arr[mid] > x:
        return binary_search(arr, x, left, mid - 1)
    else:
        return binary_search(arr, x, mid + 1, right)
    
result = binary_search(arr, x, 0, len(arr) - 1)
if result != -1:
    print(f"Element found at index: {result}")  
else:    print("Element not found in the array.")
#time complexity is O(log n) because we are halving the search space in each step