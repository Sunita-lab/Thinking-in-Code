#ek sorted array input lo
arr = list(map(int, input().split()))
# target element input lo
target_sum = int(input())

left , right = 0 , len(arr) - 1
current_sum = arr[left] + arr[right]
while left < right and current_sum != target_sum:
    if current_sum < target_sum:
        left += 1
    else:
        right -= 1
    current_sum = arr[left] + arr[right]
else:
    if current_sum == target_sum:#copilot suggest kiya ye
        print(left, right)
    else:
        print(-1, -1) #maine socha tha sirf ek

