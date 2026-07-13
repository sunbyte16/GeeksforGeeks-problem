class Solution:
    def minOperations(self, b):
        # code here
        import math
        MODULO = 10**9 + 7
        n = len(b)
        cycle_lengths = set()
        for i in range(n):
            curr_length = 0
            while b[i]:
                b[i], i = 0, b[i] - 1
                curr_length += 1
            if curr_length:
                cycle_lengths.add(curr_length)
        cycle_lcm = 1
        for cycle_length in cycle_lengths:
            cycle_lcm = math.lcm(cycle_lcm, cycle_length) % MODULO
        return cycle_lcm
