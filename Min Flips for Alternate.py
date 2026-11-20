class Solution:
     def minFlips(self, s):
          # Code here
          n = len(s)
          one_zero_count = 0
          zero_one_count = 0

          i = 0
          j = i+1

          while i < n:
               # 1st: One, 2nd: Zero
               if s[i] == '1':
                    zero_one_count += 1
               elif s[i] == '0':
                    one_zero_count += 1

               i += 2

          while j < n:
               if s[j] == '0':
                    zero_one_count += 1
               elif s[j] == '1':
                    one_zero_count += 1

               j += 2

          return min(zero_one_count, one_zero_count)
