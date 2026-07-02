class Solution:
    def stockBuySell(self, arr):
        # code here
        profit = 0
        for i in range (1, len(arr)):
            if arr[i] > arr[i-1]:
                profit += arr[i]- arr[i-1]
        return profit    