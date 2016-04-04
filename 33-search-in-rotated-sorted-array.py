class Solution(object):

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        begin, end = 0, len(nums) -1
        while begin <= end:
            mid = (begin + end) / 2 
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                if nums[mid] > nums[end] >= target:
                    begin = mid + 1
                    continue
                else: 
                    end = mid - 1
                    continue
            else:
                if nums[mid] < nums[begin] <= target:
                    end = mid - 1
                    continue
                else:
                    begin = mid + 1
                    continue 
        return -1


if __name__ == '__main__':
    s = Solution()
    assert s.search([], 1) == -1
    assert s.search([1], 1) == 0
    assert s.search([1, 2], 1) == 0
    assert s.search([1, 2], 2) == 1
    assert s.search([3, 1, 2], 2) == 2
    assert s.search([3, 4, 1, 2], 4) == 1
    assert s.search([4,5,6,7,8,1,2,3], 8) == 4