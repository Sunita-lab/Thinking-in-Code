class Solution:
    #Function to find the days of buying and selling stock for max profit.
    def stockBuySell(self, arr):
        # code here
        n = len(arr)
        buy = 0
        sell = False
        profit = 0
        i = 1
        while i < n:
            if not sell:
                if arr[i] >= arr[buy]:
                    sell = True
                    profit += arr[i] - arr[buy]
                    if i+1 < n and arr[i+1] > arr[i]:
                        buy = i 
                        sell = False
                    
                        
            else:
                buy = i 
                sell = False
                
                    
                
            i += 1
        return profit    
        