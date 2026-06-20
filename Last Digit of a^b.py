class Solution:
    def getLastDigit(self, a, b):
        # code here
        if b=='0':
            return 1

        x = ord(a[-1])-ord('0')

        if x==0 or x==1 or x==5 or x==6:
            return x

        b = int(b)
        
        if x==4:
            if b%2:
                return 4
            else:
                return 6
        
        if x==9:
            if b%2:
                return 9
            else:
                return 1
                
        
        e = 4 if b%4==0 else b%4

        res = pow(x,e)%10

        return res
