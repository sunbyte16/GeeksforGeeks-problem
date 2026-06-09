class Solution:
    def canSeatAllPeople(self, k, seats):
        # code here
        zeros = 1  # no preceding 1 at the start
        for s in seats:
            if s:
                if zeros == 0:  # consecutive "1"
                    return False
                k -= max(0, (zeros - 1) // 2)
                zeros = 0
            else:
                zeros += 1
        k -= zeros // 2
        return k <= 0
