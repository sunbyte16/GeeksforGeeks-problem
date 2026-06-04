curr_diff = max_diff = 0
        for c in s:
            if c == "0":
                curr_diff += 1
                if curr_diff > max_diff:
                    max_diff = curr_diff
            else:
                curr_diff = max(0, curr_diff - 1)
        return max_diff if max_diff else -1
