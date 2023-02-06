class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isSame(root.left, root.right)

    # A tree is called symmetric if the left subtree must be a mirror reflection of the right subtree...
    def isSame(self, leftroot, rightroot):
        if leftroot is None and rightroot is None:
            return True
        if leftroot is None or rightroot is None:
            return False
        if leftroot.val != rightroot.val:
            return False
        # Return true if the values of root nodes are same and left as well as right subtrees are symmetric...
        return self.isSame(leftroot.left, rightroot.right) and self.isSame(leftroot.right, rightroot.left)

    # def isSymmetric(self, root: TreeNode) -> bool:
    #     if root is not None:
    #         lInverted = self.invertTree(root.left)
    #         if self.isSameTree(lInverted, root.right):
    #             return True
    #         return False
    #     return True
    #
    # def invertTree(self, root: TreeNode) -> TreeNode:
    #     if root is not None:
    #         root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
    #     return root
    #
    # def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    #     if p is not None and q is not None:
    #         if p.val == q.val:
    #             return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    #         return False
    #     if p is None and q is None:
    #         return True
    #     return False


if __name__ == '__main__':
    print(Solution().isSymmetric(
        TreeNode(1),
    ) is True)
    print(Solution().isSymmetric(
        TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3))),
    ) is True)
    print(Solution().isSymmetric(
        TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3))),
    ) is False)
