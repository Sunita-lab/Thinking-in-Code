print("Enter a decimal number:")
num = int(input())

if num == 0:
    print("0")
elif num < 0:
    print("Negative numbers are not supported.")
else:        
    bin = []
    while num > 0:
        rem = num % 2
        bin.append(rem)
        num = (num // 2)

# Reverse the list to get the correct binary representation
    bin.reverse()

# Print the binary representation
    for digit in bin:
        print(digit, end="")