class Solution:
    def exitPoint(self, mat):
        # code here
        m, n = len(mat), len(mat[0])
        d = 1+0j
        p = 0+0j
        
        while 0 <= int(p.imag) < m and 0 <= int(p.real) < n:
            r0, c0 = int(p.imag), int(p.real)
            if mat[r0][c0] == 0:
                p += d 
            else:
                d *= 1j
                mat[r0][c0] = 0
        
        r0, c0 = int(p.imag), int(p.real)
        return min(m-1, max(r0, 0)), min(n-1, max(0, c0))
