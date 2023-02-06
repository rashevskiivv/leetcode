class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        height = 0

        def count(r: TreeNode, h: int) -> (int, bool):
            if r is not None:
                if r.left is None and r.right is None:
                    return h+1, True

                lc, lfl = count(r.left, h)
                rc, rfl = count(r.right, h)

                h += 1
                if lfl and rfl:
                    return h + min(lc, rc), True
                if rfl:
                    return h + rc, True
                if lfl:
                    return h + lc, True
                return h + max(lc, rc), False
            return 0, False

        height, _ = count(root, height)
        return height


if __name__ == '__main__':
    print(Solution().minDepth(
        TreeNode(3,
                 TreeNode(9),
                 TreeNode(20, TreeNode(15), TreeNode(7)))
    ))
    print(Solution().minDepth(
        TreeNode(2,
                 TreeNode(3,
                          TreeNode(4,
                                   TreeNode(5,
                                            TreeNode(6)
                                            )
                                   )
                          )
                 )
    ))
    print(Solution().minDepth(
        TreeNode(1,
                 TreeNode(2, TreeNode(4), TreeNode(5)),
                 TreeNode(3))
    ))
    print(Solution().minDepth(
        TreeNode(1,
                 TreeNode(2,
                          TreeNode(3, TreeNode(6)),
                          TreeNode(4)),
                 TreeNode(5))))
