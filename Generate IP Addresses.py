class Solution:
    def generateIp(self, s):
        res = []
        n = len(s)

        def valid(part):
            if len(part) > 1 and part[0] == '0':
                return False
            return int(part) <= 255

        for i in range(1, min(4, n)):
            for j in range(i+1, min(i+4, n)):
                for k in range(j+1, min(j+4, n)):
                    
                    a = s[:i]
                    b = s[i:j]
                    c = s[j:k]
                    d = s[k:]

                    if valid(a) and valid(b) and valid(c) and valid(d):
                        res.append(a + "." + b + "." + c + "." + d)

        return res
