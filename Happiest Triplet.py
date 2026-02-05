class Solution:
    def smallestDiff(self, a, b, c):
        a.sort()
        b.sort()
        c.sort()

        i = j = k = 0
        best_diff = float('inf')
        best_sum = float('inf')
        best_triplet = []

        while i < len(a) and j < len(b) and k < len(c):
            x, y, z = a[i], b[j], c[k]
            curr_min = min(x, y, z)
            curr_max = max(x, y, z)
            diff = curr_max - curr_min
            total = x + y + z

            if diff < best_diff or (diff == best_diff and total < best_sum):
                best_diff = diff
                best_sum = total
                best_triplet = [x, y, z]

            # Move pointer of minimum element
            if curr_min == x:
                i += 1
            elif curr_min == y:
                j += 1
            else:
                k += 1

        # Return in decreasing order
        return sorted(best_triplet, reverse=True)
