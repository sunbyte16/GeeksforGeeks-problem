class Solution:
    def optimalArray(self, arr):
        # code here
        n = len(arr)
        for i in range(n-1,-1,-1):
            if i%2==0:
                arr[i] = abs(arr[i]-arr[i//2])
            else:
                av1 = (arr[i//2]+arr[(i//2)+1])//2
                arr[i] = abs(arr[i]-av1)+abs(av1-arr[i//2])
            
        for i in range(1,n):
            arr[i] = arr[i]+arr[i-1]
            
        return arr
