# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def dfs(self, node):
		if node is None:
			return 0
		lmax = self.dfs(node.left)
		rmax = self.dfs(node.right)
		self.max = max(lmax+rmax+node.val, self.max)
		return max(lmax+node.val, rmax+node.val, 0)

	def maxPathSum(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		self.max = None
		self.dfs(root)
		return self.max
