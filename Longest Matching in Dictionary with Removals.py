class Solution:
    def findLongestWord(self, s: str, d: list) -> str:
        # code here
        from bisect import bisect_left

        chars = [[] for _ in range(26)]
        for i, e in enumerate(s):
            idx = ord(e)-ord('a')
            chars[idx].append(i)

        def ok(ss, chars):
            start = 0
            for e in ss:
                lst = chars[ord(e)-ord('a')]
                i = bisect_left(lst, start)
                if i == len(lst):
                    return False
                start = lst[i]+1
            return True

        ret = ""
        for ss in d:
            if ok(ss, chars):
                if len(ss) > len(ret):
                    ret = ss
                elif len(ss) == len(ret):
                    ret = min(ret, ss)

        return ret
