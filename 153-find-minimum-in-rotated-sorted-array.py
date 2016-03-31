class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        begin, end = 0, len(nums)-1

        while begin < end:
            if nums[begin] < nums[end]:
                return nums[begin]
            if begin+1 == end:
                return min(nums[begin], nums[end])
            mid = (begin + end) / 2
            if nums[mid] < nums[mid - 1] and nums[mid] < nums[mid + 1]:
                return nums[mid]
            if nums[mid] > nums[begin]:
                begin = mid + 1
            else:
                end = mid - 1
        return nums[begin]


if __name__ == '__main__':
    s = Solution()
    assert s.findMin([1]) == 1
    assert s.findMin([1, 2]) == 1
    assert s.findMin([2, 1]) == 1
    assert s.findMin([3, 1, 2]) == 1
    assert s.findMin([0, 1, 2]) == 0
    assert s.findMin([3, 0, 1, 2]) == 0