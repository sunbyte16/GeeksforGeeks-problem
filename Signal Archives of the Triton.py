import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
q = int(input())

B = 30
L = [0]
R = [0]
C = [0]
root = [0]

def insert(old, x):
    new = len(C)
    L.append(L[old])
    R.append(R[old])
    C.append(C[old] + 1)

    cur, prev = new, old

    for b in range(B, -1, -1):
        bit = (x >> b) & 1

        if bit == 0:
            p = L[prev]
            z = len(C)
            L.append(L[p])
            R.append(R[p])
            C.append(C[p] + 1)
            L[cur] = z
        else:
            p = R[prev]
            z = len(C)
            L.append(L[p])
            R.append(R[p])
            C.append(C[p] + 1)
            R[cur] = z

        prev = p
        cur = z

    return new

for x in a:
    root.append(insert(root[-1], x))

def get_max(r, l, x):
    u, v = root[r], root[l - 1]
    ans = 0

    for b in range(B, -1, -1):
        bit = (x >> b) & 1

        if bit == 0:
            ur, vr = R[u], R[v]
            if C[ur] - C[vr]:
                ans |= 1 << b
                u, v = ur, vr
            else:
                u, v = L[u], L[v]
        else:
            ul, vl = L[u], L[v]
            if C[ul] - C[vl]:
                ans |= 1 << b
                u, v = ul, vl
            else:
                u, v = R[u], R[v]

    return ans

for _ in range(q):
    l, r, x = map(int, input().split())
    print(get_max(r, l, x))
