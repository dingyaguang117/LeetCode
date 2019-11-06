class Solution(object):

    def countLTE(self, num, m, n):
        count = 0
        for i in range(1, m + 1):
            count += min((num // i), n)
        # print 'count %s %s %s: %s' % (num, m, n, count)
        return count

    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """

        best = None
        start, end = 1, m * n
        while start <= end:
            # print start, end
            mid = (start + end) // 2
            count = self.countLTE(mid, m, n)
            if count >= k:
                best = mid
                end = mid - 1
            elif count < k:
                start = mid + 1
        return best



if __name__ == '__main__':
    solution = Solution()
    print solution.countLTE(7, 3, 3)
    print solution.findKthNumber(3, 3, 5)
    print solution.findKthNumber(2, 3, 6)