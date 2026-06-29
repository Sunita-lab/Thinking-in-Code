class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        #code here
        items = [0]*(len(val))
        for i in range (len(val)):
            items[i] = [val[i], wt[i]]
        items.sort(key=lambda x: x[0]/x[1], reverse=True)        
        
        maximum = 0
        i = 0
        
        while capacity > 0 and i<len(val):
            if items[i][1] <= capacity:
                maximum += items[i][0]
                capacity -= items[i][1]
            else:
                maximum += capacity*(items[i][0]/items[i][1])
                capacity -= capacity
            i += 1
        return (round(maximum, 6))    
                    
            
            
            