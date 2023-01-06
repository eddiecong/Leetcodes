# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output, level = [], [root]
        while root and level:
            output.append([node.val for node in level])
            level = [kid for node in level for kid in (node.left, node.right) if kid]
        return output
