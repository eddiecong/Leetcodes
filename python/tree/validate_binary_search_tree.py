# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        output = []
        output = self.save_node(root, output)
        for i in range(1, len(output)):
            if output[i] <= output[i-1]:
                return False
        return True
    
    def save_node(self, root, output_list):
        if root is None:
            return
        
        self.save_node(root.left, output_list)
        output_list.append(root.val)
        self.save_node(root.right, output_list)
        return output_list
