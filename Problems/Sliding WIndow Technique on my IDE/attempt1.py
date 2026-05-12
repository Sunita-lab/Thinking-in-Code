#array input lo
print("Enter the array elements separated by space:")
a = list(map(int, input().split()))

#k input lo
print("Enter the value of k:")
k = int(input())

current_sum = 0
for i in range(k):
    current_sum += a[i]
max_sum = current_sum    

for i in range(0,len(a) - k):
    
    current_sum = current_sum - a[i] + a[i + k]
    max_sum = max(max_sum, current_sum)
print(max_sum)