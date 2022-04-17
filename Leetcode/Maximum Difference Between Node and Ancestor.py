#1026. Maximum Difference Between Node and Ancestor

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Node:
    def __init__(self, min_val, max_val):
        self.min_val = min_val
        self.max_val = max_val
        
class Solution:
    ans = 0
    def solve(self, root):
        if root is None:
            return None
        
        node1 = self.solve(root.left) 
        node2 = self.solve(root.right)
        
        if node1 and node2:
            min_val = min(node1.min_val, node1.max_val, node2.min_val, node2.max_val)
            max_val = max(node1.min_val, node1.max_val, node2.min_val, node2.max_val)
        elif node1:
            min_val = node1.min_val
            max_val = node1.max_val
        elif node2:
            min_val = node2.min_val
            max_val = node2.max_val
        else:
            return Node(root.val, root.val)
        
        self.ans = max(self.ans, abs(root.val-min_val), abs(root.val - max_val))
        return Node(min(min_val,root.val), max(max_val,root.val))
    
    def maxAncestorDiff(self, root):
        node = self.solve(root)
        return self.ans
        

        
        
