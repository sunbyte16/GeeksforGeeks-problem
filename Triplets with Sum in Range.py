from bisect import bisect_left, bisect_right
        arr.sort()
        n = len(arr)
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                s = arr[i]+arr[j]
                k1 = bisect_left(arr, l-s)
                k1 = max(k1, j+1)
                k2 = bisect_right(arr, r-s)
                #k2 = min(k2, n)
                ans += max(0, k2-k1)
        return ans
