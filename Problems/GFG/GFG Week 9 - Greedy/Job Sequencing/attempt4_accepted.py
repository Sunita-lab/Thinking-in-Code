class Solution:
    def jobSequencing(self, deadline, profit):
        # code here
        class DisjointSet:
            def __init__(self, n):
                self.parent = list(range(n+1))
            
            def find(self, s):
                if self.parent[s] != s:
                    self.parent[s] = self.find(self.parent[s])
                return self.parent[s]
            def merge(self, u, v):
                self.parent[v] = u
            
        n = len(profit)
        jobs = list(zip(profit, deadline))
        jobs.sort(key=lambda x: x[0], reverse=True)
        
        d = max(deadline)
        ds = DisjointSet(d)
        maxjobs = 0
        totalprofit = 0
        
        for i in range (n):
            slot = ds.find(jobs[i][1])
            if slot > 0:
                ds.merge(ds.find(slot-1), slot)
                maxjobs += 1
                totalprofit += jobs[i][0]
                
        return [maxjobs, totalprofit]        