
from collections import defaultdict

class Solution:
    def calcEquation(self, equations, values, queries):

        graph = defaultdict(list)

        # Step 1: Build graph
        for (a, b), value in zip(equations, values):

            graph[a].append((b, value))
            graph[b].append((a, 1 / value))

        # Step 2: DFS function
        def dfs(start, end, visited):

            if start == end:
                return 1.0

            visited.add(start)

            for neighbor, weight in graph[start]:

                if neighbor not in visited:

                    result = dfs(neighbor, end, visited)

                    if result != -1.0:
                        return weight * result

            return -1.0

        # Step 3: Process queries
        answers = []

        for start, end in queries:

            if start not in graph or end not in graph:
                answers.append(-1.0)

            else:
                visited = set()
                result = dfs(start, end, visited)
                answers.append(result)

        return answers
