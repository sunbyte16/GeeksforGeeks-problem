n = len(s)
        if n.bit_count() == 1:
            k //= 2
        else:
            k *= 2
        if k >= n:
            return -1
        output = []
        for c in s:
            while k and output and output[-1] > c:
                output.pop()
                k -= 1
            output.append(c)
        if k:
            del output[-k:]
        return "".join(output)
