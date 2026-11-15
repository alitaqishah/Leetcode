class Solution:
    def leafSimilar(self, root1, root2):

        def getLeaves(root):
            leaves = []

            def dfs(node):
                if node is None:
                    return

                # Check if node is a leaf
                if node.left is None and node.right is None:
                    leaves.append(node.val)
                    return

                dfs(node.left)
                dfs(node.right)

            dfs(root)
            return leaves

        leaves1 = getLeaves(root1)
        leaves2 = getLeaves(root2)

        return leaves1 == leaves2