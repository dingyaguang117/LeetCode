'''
class Solution:
	# @param {integer[]} nums
	# @return {string}

	def dfs(self, string, words):
		if not words and string > self.max:
			self.max = string
			return
		for i, word in enumerate(words):
			_string = string + word 
			if _string > self.max or self.max.startswith(_string):
				self.dfs(_string, words[:i] + words[i+1:])


	def largestNumber(self, nums):
		self.max = ''
		nums = map(str, nums)
		nums.sort(reverse=True)
		self.dfs('', nums)
		return self.max
'''

class Solution:
	# @param {integer[]} nums
	# @return {string}

	def largestNumber(self, nums):
		nums = map(str, nums)

		def cmp(a, b):
			if a==b:return 0
			if a+b<b+a:return -1
			return 1

		nums.sort(cmp=cmp, reverse=True)
		ans = ''.join(nums)
		if ans[0] == '0':
			ans = '0'
		return ans

if __name__ == '__main__':
	s = Solution()
	print s.largestNumber([3, 30, 34, 5, 9])
	print s.largestNumber([0, 0])