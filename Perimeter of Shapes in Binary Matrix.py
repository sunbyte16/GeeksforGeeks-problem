from typing import List

class Solution:
    def findPerimeter(self, mat: List[List[int]]) -> int:
        from itertools import product
        perimeter = 0
        if not mat:
            return perimeter
        n = len(mat)
        if n < 1:
            return perimeter
        m = len(mat[0])
        for i, j in product(range(n), range(m)):
            if mat[i][j] == 0: continue
            perimeter += 4
        
            if i > 0 and mat[i - 1][j] == 1: perimeter -= 2
            if j > 0 and mat[i][j - 1] == 1: perimeter -= 2
        
        return perimeter
