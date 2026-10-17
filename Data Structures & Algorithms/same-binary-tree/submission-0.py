# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            if p == None and q == None:
                return True
            if (p and q and p.val!=q.val) or (p and not q) or (not p and q):
                return False
            equalLeft = dfs(p.left, q.left)
            equalRight = dfs(p.right, q.right)

            return equalLeft and equalRight
        return dfs(p,q)
        