
class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        dp = []
        queue = []

        # 初始化 DP
        for i in range(length):
            dp.append([0] * length)

        result = ''

        # 计算 1 长度 和 2长度
        for i in range(length):
            dp[i][i] = 1
            queue.append((i, i))
            result = s[i]

        for i in range(length - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = 1
                queue.append((i, i + 1))
                result = s[i: i + 2]

        # 拓展
        while queue:
            a, b = queue.pop()
            if a == 0 or b == length - 1:
                continue

            if s[a - 1] == s[b + 1]:
                queue.append((a - 1, b + 1))
                if b - a + 3 > len(result):
                    result = s[a - 1: b + 2]
        return result


if __name__ == '__main__':
    print(Solution().longestPalindrome("abaaa"))