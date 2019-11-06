#coding=utf-8
class Solution(object):

    def __init__(self):
        self.dp = []
        self.w = 0

    def _match(self, s, p):

        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        index = len(s) * self.w + len(p)
        if self.dp[index] is not None:
            return self.dp[index]

        if s == '' and p == '':
            self.dp[index] = True
            return True

        if p == '' and s != '':
            self.dp[index] = False
            return False

        # * 的情况
        if len(p) >= 2 and p[1] == '*':
            # 匹配0次的情况
            if self._match(s, p[2:]):
                self.dp[index] = True
                return True
            # 匹配 1+次的情况
            if s =='' or p[0] == '.' or p[0] == s[0]:
                # 匹配1次的情况
                if self._match(s[1:], p[2:]):
                    self.dp[index] = True
                    return True
                # 匹配多次的情况(注意s 为空，就不做多次匹配，否则会无法停止)
                if s != '' and self._match(s[1:], p):
                    self.dp[index] = True
                    return True
        elif len(p) > 0 and len(s) > 0 and (p[0] == '.' or p[0] == s[0]):
            self.dp[index] = self._match(s[1:], p[1:])
            return self.dp[index]
        self.dp[index] = False
        return False

    def isMatch(self, s, p):
        self.dp = [None] * ((len(s) + 1) * (len(p) + 1))
        self.w = len(p) + 1
        result = self._match(s, p)
        return result


if __name__ == '__main__':
    solution = Solution()
    solution.isMatch('a', 'ab*a')