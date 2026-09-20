from collections import deque, defaultdict

class Solution:
    def areAnagrams(self, root1, root2):
        q1 = deque([root1])
        q2 = deque([root2])

        while q1 and q2:
            freq = defaultdict(int)

            for q, v in [(q1, 1), (q2, -1)]:
                for _ in range(len(q)):
                    node = q.popleft()

                    if node:
                        freq[node.data] += v
                        q.append(node.left)
                        q.append(node.right)

            if any(freq.values()):
                return False

        return not q1 and not q2
