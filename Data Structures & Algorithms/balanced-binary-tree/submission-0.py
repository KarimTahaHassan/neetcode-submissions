# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if root:
                leftSide = dfs(root.left)
                rightSide = dfs(root.right)
                balanced = leftSide[0] and rightSide[0] and abs(leftSide[1] - rightSide[1]) <= 1
                return [balanced, 1+max(leftSide[1],  rightSide[1])]

            return [True, 0]

        return dfs(root)[0]