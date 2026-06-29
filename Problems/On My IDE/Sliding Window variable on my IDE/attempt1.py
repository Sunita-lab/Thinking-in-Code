
# ek array input lo
arr = list(map(int, input("Enter the elements of the array separated by space: ").split()))

#enter the target
target = int(input("Enter the target value: "))

left, right = 0, 0
count = 0
while right < len(arr) and left <= right:
    current_sum = sum(arr[left:right+1])
    if current_sum <= target:
        count = max(count, right - left + 1)
        right += 1
    else:
        left += 1
print("The length of the longest subarray with sum less than or equal to target is:", count)        
