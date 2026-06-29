# ek array input lo
arr = list(map(int, input("Enter the elements of the array separated by space: ").split()))

#enter the target
target = int(input("Enter the target value: "))
left, right = 0, 0
count = 0
current_sum = arr[0] if arr else 0  # Initialize current_sum with the first element if it exists
while right < len(arr) and left <= right:
    if current_sum <= target:
        count = max(count, right - left + 1)
        right += 1
        if right < len(arr):  # Add the next element to current_sum if it exists
            current_sum += arr[right]
    else:
        current_sum -= arr[left]  # Subtract the leftmost element from current_sum
        left += 1
        
print("The length of the longest subarray with sum less than or equal to target is:", count)        
