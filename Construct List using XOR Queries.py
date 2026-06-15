class Solution:
    def constructList(self, queries):
        # code here
        xor_val = 0
        ans = []

        for typ, x in reversed(queries):
            if typ == 1:
                xor_val ^= x
            else:
                ans.append(x ^ xor_val)

        # Initial element 0
        ans.append(xor_val)

        ans.sort()
        return ans
