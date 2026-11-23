# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        def dfs(depth, node):
            if not node:
                return
            if len(output) == depth:
                output.append(node.val)
            dfs(depth+1, node.right)
            dfs(depth+1, node.left)
        dfs(0, root)
        return output
        