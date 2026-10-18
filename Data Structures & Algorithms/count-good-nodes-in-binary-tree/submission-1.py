# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node, mNum):
            if not node:
                return
            if node.val >= mNum:
                self.res+=1
            
            dfs(node.left, max(mNum, node.val))
            dfs(node.right, max(mNum, node.val))

            return
        dfs(root, float("-inf"))
        return self.res
            

        