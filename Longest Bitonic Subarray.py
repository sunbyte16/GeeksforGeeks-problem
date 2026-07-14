class Solution:
	def bitonic(self,arr):
		# code here
		curr_inc = curr_dec = max_len = 0
        prev = arr[0]
        for a in arr:
            if prev == a:
                curr_inc += 1
                curr_dec += 1
                max_len = max(max_len, curr_inc, curr_dec)
            elif prev < a:
                curr_inc += 1
                curr_dec = 1
                max_len = max(max_len, curr_inc)
            else:  # a < prev
                curr_dec = max(curr_inc, curr_dec) + 1
                curr_inc = 1
                max_len = max(max_len, curr_dec)
            prev = a
        return max_len
