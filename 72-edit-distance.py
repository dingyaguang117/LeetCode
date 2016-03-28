class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len1 = len(word1)
        len2 = len(word2)
        dp = [[0]*(len2+1) for i in range(len1+1)]
        for i in range(0,len1+1): dp[i][0] = i
        for i in range(0,len2+1): dp[0][i] = i
        for i in range(1,len1+1):
            for j in range(1,len2+1):
                n1 = dp[i-1][j-1]
                n2 = dp[i-1][j] + 1
                n3 = dp[i][j-1] + 1
                if word1[i-1] != word2[j-1]:n1 += 1
                dp[i][j] = min(n1,n2,n3)
        return dp[len1][len2]


if __name__ == '__main__':
	s = Solution()
	print s.minDistance("a", "a")