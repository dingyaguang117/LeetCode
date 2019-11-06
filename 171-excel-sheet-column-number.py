class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = ''.join(reversed(list(s)))
        num = 0
        for i in range(0, len(s)):
            n = ord(s[i]) - ord('A') + 1
            num += 26**i*n
        return num


solution = Solution()
print solution.titleToNumber('AA')
print solution.titleToNumber('A')