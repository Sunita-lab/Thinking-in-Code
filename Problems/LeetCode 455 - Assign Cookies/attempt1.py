class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count = 0
        n = len(g) if len(g) <= len(s) else len(s)
        for i in range (0,n):
            if g[i] <= s[i]:
                count += 1
        return count        

        