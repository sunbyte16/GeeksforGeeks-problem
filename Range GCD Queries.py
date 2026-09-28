from math import gcd

class Solution:
    def processQueries(self, arr, queries):
        n = len(arr)
        tree = [0] * (4 * n)

        def build(node, l, r):
            if l == r:
                tree[node] = arr[l]
                return

            mid = (l + r) // 2
            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)
            tree[node] = gcd(tree[node * 2], tree[node * 2 + 1])

        def update(node, l, r, idx, val):
            if l == r:
                tree[node] = val
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx, val)
            else:
                update(node * 2 + 1, mid + 1, r, idx, val)

            tree[node] = gcd(tree[node * 2], tree[node * 2 + 1])

        def query(node, l, r, ql, qr):
            if qr < l or r < ql:
                return 0

            if ql <= l and r <= qr:
                return tree[node]

            mid = (l + r) // 2

            return gcd(
                query(node * 2, l, mid, ql, qr),
                query(node * 2 + 1, mid + 1, r, ql, qr)
            )

        build(1, 0, n - 1)

        ans = []

        for q in queries:
            if q[0] == 0:
                ans.append(query(1, 0, n - 1, q[1], q[2]))
            else:
                arr[q[1]] = q[2]
                update(1, 0, n - 1, q[1], q[2])

        return ans
