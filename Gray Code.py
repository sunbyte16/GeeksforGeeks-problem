class Solution:
    def graycode(self, n):
        result = ["0", "1"]
        
        for i in range(2, n + 1):
            temp = []
            
            # prefix '0'
            for code in result:
                temp.append("0" + code)
            
            # prefix '1' to reversed
            for code in reversed(result):
                temp.append("1" + code)
            
            result = temp
        
        return result
