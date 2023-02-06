class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is not None:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


if __name__ == '__main__':
    print(Solution().invertTree(TreeNode(2, TreeNode(1), TreeNode(3))))
    print(Solution().invertTree(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))))
