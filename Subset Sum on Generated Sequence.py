class Solution:
    def isPossible(self, arr, s, x):
        if x == 0:
            return True

        # Generate numbers written on the paper
        values = []
        total = s

        values.append(s)

        for a in arr:
            new_value = total + a
            values.append(new_value)
            total += new_value

            # Once values become larger than x,
            # later values will also be larger than x.
            if new_value > x:
                break

        # Bitset subset-sum.
        # Python integers make this very fast.
        bits = 1

        for v in values:
            if v <= x:
                bits |= bits << v
                bits &= (1 << (x + 1)) - 1

        return bool((bits >> x) & 1)
