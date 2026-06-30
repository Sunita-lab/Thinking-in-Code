class Solution:    
    def minPlatform(self, arr, dep):
        # code here
        times = []
        for i in range (0, len(arr)):
            times.append([arr[i],'a'])
            times.append([dep[i], 'd'])
        times.sort(key=lambda x: x[0])
        maximum = 0
        count = 0
        it = 0
        while it < len(times):
            if times[it][1] == 'a':
                count += 1
            else:
                count -= 1
            maximum = max(maximum, count) 
            it += 1
        return maximum    
            
            
            
        
        