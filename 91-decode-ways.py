class Solution(object):

	def isLegal(self, s):
		if s[0] == '0':
			return False
		if 0 < int(s) < 27:
			return True
		return False

	def numDecodings(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		length = len(s)
		if length == 0:
			return 0

		dp = [0] * length
		dp[0] = 1 if self.isLegal(s[0]) else 0
		if length > 1:
			dp[1] = dp[0] if self.isLegal(s[1]) else 0
			if self.isLegal(s[:2]):
				dp[1] += 1

			for i in xrange(2, length):
				dp[i] = dp[i-1] if self.isLegal(s[i]) and dp[i-1] > 0 else 0
				if self.isLegal(s[i-1:i+1]) and dp[i-2]>0:
					dp[i] += dp[i-2]
		# if len(filter(lambda a: a==0, dp)) == 0:
			# return dp[length-1]
		# return 0
		return dp[length-1]

if __name__ == '__main__':
	s = Solution()
	assert s.numDecodings("0") == 0
	assert s.numDecodings("01") == 0
	assert s.numDecodings("") == 0
	assert s.numDecodings("1") == 1
	assert s.numDecodings("75") == 1
	assert s.numDecodings("12") == 2
	assert s.numDecodings("123") == 3
	assert s.numDecodings("10") == 1
	assert s.numDecodings("100") == 0
	assert s.numDecodings("101") == 1