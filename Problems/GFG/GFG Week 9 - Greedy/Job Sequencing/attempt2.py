class Solution:
    def jobSequencing(self, deadline, profit):
        # code here
        jobs = list(zip(profit, deadline))
        jobs.sort(key=lambda x: x[0], reverse=True)
        slots = [False]*(max(deadline)+1)
        slots[0] = True
        maximumjobs = 0
        totalprofit = 0
        i = 0
        while i < len(profit):
            for j in range (jobs[i][1], -1, -1):
                if not slots[j]:
                    slots[j] = True
                    maximumjobs += 1
                    totalprofit += jobs[i][0]
                    break
            i += 1
        return [maximumjobs, totalprofit]    
            