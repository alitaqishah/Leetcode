class Solution:
    def goodNodes(self, root):

        def dfs(node, max_val):

            if node is None:
                return 0

            count = 0

            # Check if current node is good
            if node.val >= max_val:
                count = 1

            # Update maximum value
            max_val = max(max_val, node.val)

            # Visit left and right subtree
            count += dfs(node.left, max_val)
            count += dfs(node.right, max_val)

            return count

        return dfs(root, root.val)