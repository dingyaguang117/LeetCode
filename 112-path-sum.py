# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

	def dfs(self, root, value, sum):
		if root is None:
			return False
		val = root.val + value
		if val == sum and root.left is None and root.right is None:
			return True
		return self.dfs(root.left, val, sum) or self.dfs(root.right, val, sum)

	def hasPathSum(self, root, sum):
		"""
		:type root: TreeNode
		:type sum: int
		:rtype: bool
		"""
		return self.dfs(root, 0, sum)
py