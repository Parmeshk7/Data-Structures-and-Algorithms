#583. Convert BST to Greater Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    curr_sum = 0
    def solve(self, root):
        if root is None:
            return
        
        self.solve(root.right)
        self.curr_sum += root.val
        root.val = self.curr_sum
        self.solve(root.left)
        
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.solve(root)
        return root
    
    
