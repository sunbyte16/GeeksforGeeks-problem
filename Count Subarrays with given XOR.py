class Solution:
    def subarrayXor(self, arr, k):
        freq = {}
        curr_xor = 0
        count = 0
        
        for num in arr:
            curr_xor ^= num
            
            # Case when prefix XOR itself equals k
            if curr_xor == k:
                count += 1
            
            # Check if there exists a prefix giving required XOR
            if (curr_xor ^ k) in freq:
                count += freq[curr_xor ^ k]
            
            # Store current prefix XOR
            freq[curr_xor] = freq.get(curr_xor, 0) + 1
        
        return count
