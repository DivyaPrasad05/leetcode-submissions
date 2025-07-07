# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(curr, currMax):
            # Base Case
            if not curr:
                return None
            # Recursive Case
            if curr.val >= currMax:
                self.res += 1
                currMax = curr.val
            dfs(curr.left, currMax)
            dfs(curr.right, currMax)
            return self.res
        
        return dfs(root, root.val)