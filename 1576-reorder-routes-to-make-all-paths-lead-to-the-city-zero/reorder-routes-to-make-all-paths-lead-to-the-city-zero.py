
class Solution:
    def minReorder(self, n, connections):

        graph = [[] for _ in range(n)]

        # Build adjacency list
        for a, b in connections:
            graph[a].append((b, 1))
            graph[b].append((a, 0))

        visited = {0}
        stack = [0]
        changes = 0

        while stack:
            city = stack.pop()

            for neighbor, cost in graph[city]:

                if neighbor not in visited:
                    visited.add(neighbor)

                    changes += cost

                    stack.append(neighbor)

        return changes
