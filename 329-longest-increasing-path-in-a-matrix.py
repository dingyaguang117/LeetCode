'''
递归+记忆化， DP
'''

class Solution(object):

	def calc(self, i, j):
		if self.dp[i][j]:
			return self.dp[i][j]
		value = self.matrix[i][j]
		ans = 0
		if i > 0 and self.matrix[i-1][j] < value:
			ans = max(ans, self.calc(i-1, j))
		if j > 0 and self.matrix[i][j-1] < value:
			ans = max(ans, self.calc(i, j-1))
		if i < self.m-1 and self.matrix[i+1][j] < value:
			ans = max(ans, self.calc(i+1, j))
		if j < self.n-1 and self.matrix[i][j+1] < value:
			ans = max(ans, self.calc(i, j+1))
		self.dp[i][j] = ans + 1
		return self.dp[i][j]

	def longestIncreasingPath(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: int
		"""
		if len(matrix) == 0 or len(matrix[0]) == 0: return 0

		self.matrix = matrix
		self.m, self.n = len(matrix), len(matrix[0])
		self.dp = [[0]*self.n for i in xrange(self.m)]

		ans = 0
		for i in xrange(self.m):
			for j in xrange(self.n):
				_ans = self.calc(i, j)
				ans = max(ans, _ans)
		return ans


if __name__ == '__main__':
	s = Solution()
	nums = [
	  [3,4,5],
	  [3,2,6],
	  [2,2,1]
	]

	print s.longestIncreasingPath(nums)