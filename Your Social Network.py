class Solution:
    def socialNetwork(self, arr):
        n = len(arr) + 1
        ans = []
        for i in range(2, n + 1):
            dist = [0] * (i + 1)
            current = i
            k = 0
            while current != 1:
                current = arr[current - 2]
                k += 1
                dist[current] = k
            for j in range(1, i):
                if dist[j] != 0:
                    ans.append([i, j, dist[j]])
        return ans
