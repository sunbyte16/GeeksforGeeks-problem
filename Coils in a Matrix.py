class Solution:
    def formCoils(self, n: int) -> list[list[int]]:
        size = 4 * n
        max_ele = size * size
        
        a1 = []
        dirs = 1
        curr = size
        fe = 1
        
        for _ in range(2 * n):
            a1.extend(range(fe, fe + (size * (curr - 1) + 1) * dirs, size * dirs))
            
            curr -= 2
            
            fe = a1[-1] + dirs
            a1.extend(range(fe, fe + curr * dirs, dirs))
            
            dirs *= -1
            fe = a1[-1] + size * dirs
        
        return [a1, [max_ele - num + 1 for num in a1]]
