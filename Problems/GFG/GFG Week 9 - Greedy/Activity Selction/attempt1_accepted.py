class Solution:
    def activitySelection(self, start, finish):
        #code here
        maximum = 1
        items = list(zip(start, finish))
        items.sort(key=lambda x: x[1])
        i = 1
        currentfinish = items[0][1]
        while i < len(items):
            if items[i][0] > currentfinish:
                maximum += 1
                currentfinish = items[i][1]
            i += 1
            
        return maximum        
            
        
        