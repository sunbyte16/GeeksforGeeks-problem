from math import gcd

class Solution:
    def RangeLCMQuery(self, arr, queries):
        
        def lcm(a, b):
            return (a * b) // gcd(a, b)

        n = len(arr)
        tree = [1] * (4 * n)

        # Build Segment Tree
        def build(node, start, end):
            if start == end:
                tree[node] = arr[start]
                return

            mid = (start + end) // 2

            build(2 * node + 1, start, mid)
            build(2 * node + 2, mid + 1, end)

            tree[node] = lcm(
                tree[2 * node + 1],
                tree[2 * node + 2]
            )

        # Update Query
        def update(node, start, end, idx, val):
            if start == end:
                tree[node] = val
                return

            mid = (start + end) // 2

            if idx <= mid:
                update(2 * node + 1, start, mid, idx, val)
            else:
                update(2 * node + 2, mid + 1, end, idx, val)

            tree[node] = lcm(
                tree[2 * node + 1],
                tree[2 * node + 2]
            )

        # Range LCM Query
        def query(node, start, end, l, r):

            # No overlap
            if r < start or end < l:
                return 1

            # Complete overlap
            if l <= start and end <= r:
                return tree[node]

            mid = (start + end) // 2

            left = query(2 * node + 1, start, mid, l, r)
            right = query(2 * node + 2, mid + 1, end, l, r)

            return lcm(left, right)

        build(0, 0, n - 1)

        ans = []

        for q in queries:

            # Update Query
            if q[0] == 1:
                _, idx, val = q
                update(0, 0, n - 1, idx, val)

            # Range Query
            else:
                _, l, r = q
                ans.append(query(0, 0, n - 1, l, r))

        return ans

