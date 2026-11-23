
class Solution:
    def deleteNode(self, root, key):

        # Base case: Node does not exist
        if root is None:
            return None

        # Search in left subtree
        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        # Search in right subtree
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        # Node found
        else:

            # Case 1 and Case 2:
            # No left child
            if root.left is None:
                return root.right

            # No right child
            if root.right is None:
                return root.left

            # Case 3: Two children
            successor = root.right

            while successor.left:
                successor = successor.left

            root.val = successor.val

            root.right = self.deleteNode(
                root.right, successor.val
            )

        return root
