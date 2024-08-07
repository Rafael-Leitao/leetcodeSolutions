# Definition for a binary tree node
# Use pip install binarytree on terminal
from binarytree import build

# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def invertTree(self, root):

        if not root:
            return None
        
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


tree_list = [4,2,7,1,3,6,9]
root = build(tree_list)

sol = Solution()
print(sol.invertTree(root))  # Output: [4,7,2,9,6,3,1]
