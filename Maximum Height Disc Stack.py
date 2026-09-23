class Solution:
    def maxStackHeight(self, r, h):
        discs = sorted(zip(r, h))

        vals = sorted(set(h))
        pos = {v: i + 1 for i, v in enumerate(vals)}

        bit = [0] * (len(vals) + 1)

        def query(i):
            ans = 0
            while i:
                ans = max(ans, bit[i])
                i -= i & -i
            return ans

        def update(i, val):
            while i < len(bit):
                bit[i] = max(bit[i], val)
                i += i & -i

        ans = 0
        i = 0

        while i < len(discs):
            j = i
            group = []

            while j < len(discs) and discs[j][0] == discs[i][0]:
                j += 1

            for k in range(i, j):
                rad, ht = discs[k]
                best = query(pos[ht] - 1)
                group.append((pos[ht], best + ht))
                ans = max(ans, best + ht)

            for p, val in group:
                update(p, val)

            i = j

        return ans
