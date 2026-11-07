class Solution:
    def generateUsernames(self, arr: list[str]) -> list[str]:
        used_names = {a: 0 for a in arr}
        ans = []

        for a in arr:
            if used_names[a] == 0:
                ans.append(a)
                used_names[a] = 1
            else:
                i = used_names[a]

                while a + str(i) in used_names:
                    i += 1

                b = a + str(i)
                ans.append(b)

                used_names[a] = i + 1
                used_names[b] = 1

        return ans
