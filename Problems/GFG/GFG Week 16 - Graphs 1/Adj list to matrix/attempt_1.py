class Solution: 
    def adjToMat(self, adj):
        # code here
        n = len(adj)
        mat = [[0 for _ in range(n)] for _ in range(n)]
        for i in range (len(adj)):
            for j in range (len(adj[i])):
                mat[i][adj[i][j]] = 1
        return mat        
                
                