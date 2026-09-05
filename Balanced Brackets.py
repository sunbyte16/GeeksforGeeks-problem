#Hackerrank Problems

import os
import sys


def isBalanced(s):
    stack = []

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for ch in s:
        if ch in '([{':
            stack.append(ch)
        else:
            if not stack or stack[-1] != pairs[ch]:
                return "NO"
            stack.pop()

    if stack:
        return "NO"

    return "YES"


if __name__ == '__main__':
    # HackerRank normally provides OUTPUT_PATH
    output_path = os.environ.get('OUTPUT_PATH')

    t = int(input().strip())

    results = []

    for _ in range(t):
        s = input().strip()
        results.append(isBalanced(s))

    if output_path:
        with open(output_path, 'w') as fptr:
            fptr.write('\n'.join(results) + '\n')
    else:
        print('\n'.join(results))
