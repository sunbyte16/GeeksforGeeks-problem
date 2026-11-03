class Solution:
    def maximumWeight(self, n, edges, queries):
        parent = list(range(n + 1))
        size = [1] * (n + 1)

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        edges.sort(key=lambda x: x[2])

        indexed_queries = sorted(
            (x, i) for i, x in enumerate(queries)
        )

        ans = [0] * len(queries)
        total = 0
        j = 0

        for weight, idx in indexed_queries:
            while j < len(edges) and edges[j][2] <= weight:
                u, v, w = edges[j]

                pu = find(u)
                pv = find(v)

                if pu != pv:
                    total += size[pu] * size[pv]

                    if size[pu] < size[pv]:
                        pu, pv = pv, pu

                    parent[pv] = pu
                    size[pu] += size[pv]

                j += 1

            ans[idx] = total

        return ans
