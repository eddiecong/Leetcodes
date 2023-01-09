# Key Idea:
# 1. Recursively solve the question.


# Reference Link:
# Question name: 144. Binary Tree Preorder Traversal
# https://leetcode.com/problems/binary-tree-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer_list = []

        def dfs(tree):
            if tree is None: return
            answer_list.append(tree.val)
            dfs(tree.left)
            dfs(tree.right)

        dfs(root)
        return answer_list
