class Solution:
    def minCandy(self, arr):
        # Code here
        ans = [1]*len(arr)
        for i in range (1, len(arr)):
            if arr[i-1] < arr[i]:
                ans[i] = ans[i-1] + 1
        for i in range (len(arr)-2, -1, -1):
            if arr[i] > arr[i+1] and ans[i] <= ans[i+1]:
                ans[i] = ans[i+1] + 1
        return sum(ans)        
                
            