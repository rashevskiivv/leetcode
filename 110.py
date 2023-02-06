class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is not None:
            l, r = root.left, root.right
            lh = self.maxDepth(l)
            rh = self.maxDepth(r)
            if -1 <= lh - rh <= 1:
                return self.isBalanced(l) and self.isBalanced(r)
            return False
        return True

    def maxDepth(self, root: TreeNode) -> int:
        height = 0

        def count(r: TreeNode, h: int) -> int:
            if r is not None:
                lc = count(r.left, h)
                rc = count(r.right, h)
                h += 1
                return h + max(lc, rc)
            return 0

        return count(root, height)


if __name__ == '__main__':
    print(
        Solution().isBalanced(TreeNode())
    )
    print(
        Solution().isBalanced(
            TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        )
    )
    print(
        Solution().isBalanced(
            TreeNode(1, TreeNode(2, TreeNode(13, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))
        )
    )
    print(
        Solution().isBalanced(
            TreeNode(1,
                     TreeNode(2, TreeNode(3, TreeNode(4))),
                     TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
        )
    )
