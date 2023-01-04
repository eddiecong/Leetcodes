# Key Idea:
# 1. Need to take the edge case into consideration.
# 2. Edge case, like the root node is None.
# 3. Node list to hold the tree nodes and level to hold levels.

# Reference Link:
# Question name: 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        nodes, level = [root], 0
        while len(nodes) != 0:
            tmp = []
            for node in nodes:
                if node.left is not None:
                    tmp.append(node.left)
                if node.right is not None:
                    tmp.append(node.right)
            level += 1
            nodes = tmp
        return level
