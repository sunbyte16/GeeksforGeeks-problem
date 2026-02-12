class Solution():
    def maxMinHeight(self, arr, k, w):
        n = len(arr)

        # Helper function to check if we can achieve at least 'target' height
        def canAchieve(target):
            temp = [0] * (n + 1)   # difference array
            curr_add = 0
            water_used = 0

            for i in range(n):
                curr_add += temp[i]
                current_height = arr[i] + curr_add

                if current_height < target:
                    need = target - current_height
                    water_used += need

                    if water_used > k:
                        return False

                    curr_add += need
                    if i + w < n:
                        temp[i + w] -= need

            return True

        left = min(arr)
        right = min(arr) + k
        ans = left

        while left <= right:
            mid = (left + right) // 2

            if canAchieve(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
