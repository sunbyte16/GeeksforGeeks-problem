from collections import deque

n, m = map(int, input().split())
a = list(map(int, input().split()))

mn, mx = deque(), deque()
best = float('inf')
pos = 1

for i in range(n):
    while mn and a[mn[-1]] >= a[i]:
        mn.pop()
    while mx and a[mx[-1]] <= a[i]:
        mx.pop()

    mn.append(i)
    mx.append(i)

    if mn[0] <= i - m:
        mn.popleft()
    if mx[0] <= i - m:
        mx.popleft()

    if i >= m - 1:
        diff = a[mx[0]] - a[mn[0]]
        start = i - m + 2

        if diff < best:
            best = diff
            pos = start

print(best, pos)
