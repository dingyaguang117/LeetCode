class Solution(object):

	def calc(self, pos):
		if self.gives[pos]:
			return self.gives[pos]
		ans = 0
		if pos != 0 and self.ratings[pos-1] < self.ratings[pos]:
			ans = max(self.calc(pos-1), ans)
		if pos != self.length -1 and self.ratings[pos+1] < self.ratings[pos]:
			ans = max(self.calc(pos+1), ans)

		self.gives[pos] = ans + 1
		return self.gives[pos]
		

	def candy(self, ratings):
		import sys
		sys.setrecursionlimit(100000)
		self.ratings = ratings
		self.length = len(ratings)
		self.gives = [0] * self.length
		for i in xrange(self.length):
			self.calc(i)
		return sum(self.gives)


if __name__ == '__main__':
	s = Solution()
	x = [1, 2, 3, 4, 5, 6]
	assert s.candy(x) == 21

