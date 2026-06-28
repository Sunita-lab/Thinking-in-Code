class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        count = 0
    
        s.sort()
        
        greedy, satisfied = 0, 0
        while greedy < len(g) and satisfied < len(s):
            if g[greedy] <= s[satisfied]:
                count += 1
                greedy += 1
                satisfied += 1
            else:
                satisfied += 1
        return count            




        