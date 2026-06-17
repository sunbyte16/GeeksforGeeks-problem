class Solution:
    def maxProduct(self, n):
        # code here
        if n < 4:
            return [0, 0, 1, 2, 4][n]
        q, r = divmod(n, 3)
        match r:
            case 0:
                return 3**q
            case 1:
                return 3**(q - 1) * 4
            case 2:
                return 3**q * 2
