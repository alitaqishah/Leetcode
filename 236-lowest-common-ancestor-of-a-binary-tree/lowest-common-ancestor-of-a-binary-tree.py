# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = {root: None}
        stack = [root]

        # Build parent pointers until both p and q are found
        while p not in parent or q not in parent:
            node = stack.pop()

            if node.left:
                parent[node.left] = node
                stack.append(node.left)

            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        # Store all ancestors of p
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]

        # Climb from q until finding a common ancestor
        while q not in ancestors:
            q = parent[q]

        return q