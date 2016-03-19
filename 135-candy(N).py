class Solution(object):
	def calc(self, L):
		length = len(L)
		ans = [1] * length
		for i in xrange(1, length):
			if L[i] > L[i-1]:
				ans[i] = ans[i-1] + 1
		return ans
	def candy(self, ratings):
		ans1 = self.calc(ratings)
		ans2 = list(reversed(self.calc(list(reversed(ratings)))))
		ans = map(lambda item: max(item), zip(ans1, ans2))
		return sum(ans)




if __name__ == '__main__':
	s = Solution()

	assert s.candy([1,2,3,4,5,6]) == 21
	assert s.candy([1]) == 1
	assert s.candy([1, 1]) == 2
	assert s.candy([1, 2]) == 3
	assert s.candy([1, 2, 1]) == 4
