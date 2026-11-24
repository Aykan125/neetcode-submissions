# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = root.val
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            self.maxSum = max(self.maxSum, left + node.val, right+node.val, left+right+node.val)
            return max(left+node.val, right+node.val, node.val, 0)
        dfs(root)
        return self.maxSum
        