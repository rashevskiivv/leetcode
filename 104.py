class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
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
        Solution().maxDepth(
            TreeNode(1, None, TreeNode(2))
        )
    )
    print(
        Solution().maxDepth(
            TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        )
    )
