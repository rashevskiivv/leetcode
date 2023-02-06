class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is not None and q is not None:
            if p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            return False
        if p is None and q is None:
            return True
        return False


if __name__ == '__main__':
    print(Solution().isSameTree(
        TreeNode(2, None, TreeNode(4)),
        TreeNode(2, TreeNode(3), TreeNode(4)),
    ) is False)
    print(Solution().isSameTree(
        None,
        None,
    ) is True)
    print(Solution().isSameTree(
        TreeNode(1, TreeNode(2), TreeNode(3)),
        TreeNode(1, TreeNode(2), TreeNode(3)),
    ) is True)
    print(Solution().isSameTree(
        TreeNode(1, TreeNode(2)),
        TreeNode(1, right=TreeNode(2)),
    ) is False)
    print(Solution().isSameTree(
        TreeNode(1, TreeNode(2), TreeNode(1)),
        TreeNode(1, TreeNode(1), TreeNode(2)),
    ) is False)
