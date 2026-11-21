
from collections import deque

class Solution:
    def maxLevelSum(self, root):
        queue = deque([root])

        level = 1
        answer = 1
        max_sum = float('-inf')

        while queue:
            level_size = len(queue)
            current_sum = 0

            for i in range(level_size):
                node = queue.popleft()

                current_sum += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            if current_sum > max_sum:
                max_sum = current_sum
                answer = level

            level += 1

        return answer
