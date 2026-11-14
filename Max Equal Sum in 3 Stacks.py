class Solution:
    def maxEqualSum(self, s1, s2, s3):
        sum1 = sum(s1)
        sum2 = sum(s2)
        sum3 = sum(s3)

        i = j = k = 0

        while True:
            if sum1 == sum2 == sum3:
                return sum1

            if sum1 >= sum2 and sum1 >= sum3:
                if i == len(s1):
                    return 0
                sum1 -= s1[i]
                i += 1

            elif sum2 >= sum1 and sum2 >= sum3:
                if j == len(s2):
                    return 0
                sum2 -= s2[j]
                j += 1

            else:
                if k == len(s3):
                    return 0
                sum3 -= s3[k]
                k += 1
