# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        self.depth = 0
        def dfs(node):

            if not node:
                return None
            if self.depth == len(res):
                res.append(node.val)
            
            self.depth+=1
            dfs(node.right)
            dfs(node.left)
            self.depth-=1
        dfs(root)
        return res
        