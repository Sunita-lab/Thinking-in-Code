class Solution:
    def jobSequencing(self, deadline, profit):
        # code here
        jobs = list(zip(profit, deadline))
        jobs.sort(key=lambda x: x[0], reverse=True)
        maxtime = jobs[0][1]
        maximumjobs = 1
        totalprofit = jobs[0][0]
        i = 1
        while i < len(jobs):
            if jobs[i][1] <= maxtime and maxtime - maximumjobs > 0:
                maxtime -= 1
                maximumjobs += 1
                totalprofit += jobs[i][0]
            elif jobs[i][1] > maxtime:
                maximumjobs += 1
                totalprofit += jobs[i][0]
            i += 1
        return [maximumjobs, totalprofit]    
                
                
                
        