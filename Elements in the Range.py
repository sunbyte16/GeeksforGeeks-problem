class Solution:
    def checkElements(self, start, end, arr):
        sum_e = 0
        found = 0
        i = start
        for e in arr:
            if((e<=end) and (e>=start) and (i<=end)):
                sum_e += i - e
                #print(e,i)
                i += 1
                found = 1
        i -= 1
        #print(i)        
        if(found and (not sum_e) and (i == end)):
            return True
        return False    
