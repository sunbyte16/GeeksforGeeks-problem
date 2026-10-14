class Solution:
    def findRollOut(self, s, roll):
        # code here
        ops = [0]*len(s)
        for e in roll:
            ops[0] += 1 
            if e < len(s):
                ops[e] -= 1 

        op, ret = 0, []
        for i, e in enumerate(s):
            op += ops[i] 
            c = chr((ord(e) - ord('a') + op)%26 + ord('a'))
            ret.append(c)
        return ''.join(ret)
