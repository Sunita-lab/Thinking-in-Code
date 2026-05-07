#user ke hisab se input lena hai
arr = list(map(int, input("Enter the sorted array (space separated): ").split()))
target = int(input("Enter the target element: "))
def binary_search(left, right, target):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

result = binary_search(0, len(arr) - 1, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")