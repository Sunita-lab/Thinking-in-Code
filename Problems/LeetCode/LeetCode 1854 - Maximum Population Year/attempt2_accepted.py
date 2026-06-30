class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        times = []
        maxforyears = []
        for i in range (len(logs)):
            times.append([logs[i][0], 'b'])
            times.append([logs[i][1], 'a'])

        times.sort(key=lambda x: (x[0], x[1]))
        maximum = 0
        count = 0
        i = 0
        while i in range (len(times)):
            if times[i][1] == 'b':
                count += 1
            else:
                count -= 1
                
            maximum = max(maximum, count) 
            maxforyears.append([times[i][0], count])  
            i += 1
        earliest = min([x for x in maxforyears if x[1] == maximum])    
        return earliest[0]         

        
        