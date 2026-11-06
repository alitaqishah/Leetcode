from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        row_count = Counter(tuple(row) for row in grid)

        count = 0

        for col in zip(*grid):
            count += row_count[tuple(col)]

        return count