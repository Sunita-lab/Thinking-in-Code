#user se input lena hai
print("Enter the elements of the unimodal array: ")
arr = list(map(int, input().split()))

def ternary_search(arr):
    left, right = 0, len(arr)-1
    mid = (left + right) // 2
    while left != right:
        mid1 = (left + mid) // 2
        mid2 = (right + mid) // 2
        if mid1 < mid2:
            left = mid1
        elif mid1 > mid2:
            right = mid2
        else:
            left = mid1
            right = mid2

    else:
        return left

result = ternary_search(arr)
print(f"The peak element is : {result}")                    




