# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def solve(preorder, low, high):
    if len(preorder) ==  0 or (preorder[-1] < low or preorder[-1] > high):
        return None
    
    node_val = preorder.pop()
    left = solve(preorder, low, node_val)
    right = solve(preorder, node_val, high)
    
    return TreeNode(node_val, left, right)

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        preorder.reverse()
        #print(preorder)
        return solve(preorder, 1, 1000)
        
        
