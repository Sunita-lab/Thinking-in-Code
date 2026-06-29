#user se input lena hai
print("Enter the elements of the unimodal array: ")
arr = list(map(int, input().split()))

def ternary_search(arr):
    left, right = 0, len(arr)-1
    
    while left != right:
        m = (right - left + 1)//3
        mid1 = left + m
        mid2 = right - m
        if arr[mid1] < arr[mid2]:
            left = mid1 + 1
        elif arr[mid1] > arr[mid2]:
            right = mid2 - 1
        else:
            left = mid1
            right = mid2

    else:
        return left

result = ternary_search(arr)
print(f"The peak element is : {arr[result]} at index: {result}")                    




