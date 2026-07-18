class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import deque
        q = deque()
        count = {char: 0 for char in s}
        for i in range(len(s)):
            q.append(i)
            count[s[i]] += 1
            while q and count[s[q[0]]] > 1:
                q.popleft()
        return q[0] if q else -1    

        