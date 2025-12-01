class Solution:
    class TrieNode:
        __slots__ = ("child", "cnt")
        def __init__(self):
            self.child = [None, None]
            self.cnt = 0

    def cntPairs(self, arr, k):
        if k <= 0:
            return 0

        MAX_BIT = 16  # enough for values up to ~1e5

        root = self.TrieNode()

        def insert(x):
            node = root
            for b in range(MAX_BIT, -1, -1):
                bit = (x >> b) & 1
                if not node.child[bit]:
                    node.child[bit] = self.TrieNode()
                node = node.child[bit]
                node.cnt += 1

        def count_less_than_k(x):
            node = root
            res = 0
            for b in range(MAX_BIT, -1, -1):
                if not node:
                    break
                xb = (x >> b) & 1
                kb = (k >> b) & 1

                if kb == 1:
                    # XOR bit must be 0 here; take all y with bit == xb
                    same = node.child[xb]
                    if same:
                        res += same.cnt
                    # move to branch where XOR bit == 1 to keep equality so far
                    node = node.child[1 ^ xb]
                else:
                    # kb == 0: XOR bit must be 0, so only go to xb branch
                    node = node.child[xb]
            return res

        ans = 0
        for x in arr:
            ans += count_less_than_k(x)
            insert(x)

        return ans
