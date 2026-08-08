class Solution:
    def minEdgesReq(self, n, edges):
        # code here
        if len(edges) < n - 1:
            return -1
        parent = list(range(n))

        def find(u: int) -> int:
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]

        components = n
        for u, v in edges:
            u, v = find(u), find(v)
            if u != v:
                parent[u] = v
                components -= 1
        return components - 1
