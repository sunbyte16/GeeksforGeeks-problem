from itertools import product

class Solution:
    def searchWord(self, mat, word):
      ##Code here##
        n = len(mat)
        m = len(mat[0])
        k = len(word) - 1

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        result = []

        for x in range(n):
            for y in range(m):

                # First character must match
                if mat[x][y] != word[0]:
                    continue

                for dx, dy in directions:
                    end_x = x + k * dx
                    end_y = y + k * dy

                    # Check boundaries
                    if not (0 <= end_x < n and 0 <= end_y < m):
                        continue

                    found = True

                    for i in range(1, len(word)):
                        nx = x + i * dx
                        ny = y + i * dy

                        if mat[nx][ny] != word[i]:
                            found = False
                            break

                    if found:
                        result.append((x, y))
                        break

        return result
