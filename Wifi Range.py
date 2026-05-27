class Solution:
    def wifiRange(self, s, x):
        gaps = ('0' * x + s + '0' * x).split('1')
        return max(map(len, gaps)) <= 2 * x
 
