class Solution:
    def goodIndices(self, arr):
        n = len(arr)
        state = [0] * n
        ans = 0

        for start in range(n):
            if state[start] != 0:
                continue

            path = []
            cur = start

            while 0 <= cur < n and state[cur] == 0:
                state[cur] = 1
                path.append(cur)

                if arr[cur] == 0:
                    break

                cur += arr[cur]

            if not (0 <= cur < n):
                result = 2
            elif state[cur] == 1:
                result = 3
            else:
                result = state[cur]

            for idx in reversed(path):
                if arr[idx] == 0:
                    state[idx] = 3
                else:
                    state[idx] = result
                result = state[idx]

            ans += sum(state[idx] == 2 for idx in path)

        return ans
