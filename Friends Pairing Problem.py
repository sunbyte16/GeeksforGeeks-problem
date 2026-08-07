class Solution:
    def countFriendsPairings(self, n: int) -> int:
        # code here 
        if n <= 2: return n
        a, b = 1, 2
        for i in range(3, n + 1):
            a, b = b, b + (i - 1) * a
        return b
