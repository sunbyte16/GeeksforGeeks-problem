class Solution:
    def largestSumCycle(self, edge):
        # code here
        
        ans = -1
        def dfs(v, path = {}, sum=0):
            nonlocal edge, ans
            if v == -1:
                return 
            
            sum += v
            if v in path:
                ans = max(ans, sum - path[v])
                return
            path[v] = sum
            dfs(edge[v], path, sum)
            edge[v] = -1
            path.pop(v)
        
        for i in edge:
            if edge[i] != -1:
                dfs(i)
        return ans
