class Solution:
    def pathSum(self, root, targetSum):

        def countPaths(node, remaining):

            if node is None:
                return 0

            remaining -= node.val

            count = 0

            if remaining == 0:
                count += 1

            count += countPaths(node.left, remaining)
            count += countPaths(node.right, remaining)

            return count

        if root is None:
            return 0

        return (
            countPaths(root, targetSum)
            + self.pathSum(root.left, targetSum)
            + self.pathSum(root.right, targetSum)
        )