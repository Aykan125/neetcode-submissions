# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxD = 0
        def dfs(node):
            if not node:
                return 0
            
            n1 = dfs(node.left)
            n2 = dfs(node.right)
            curMax = n1 + n2
            self.maxD = max(curMax, self.maxD)

            return 1 + max(n1, n2)
        dfs(root)
        return self.maxD
        