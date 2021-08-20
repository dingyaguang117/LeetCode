from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        s = set()

        for mid in range(1, len(nums) - 1):
            start, end = 0, len(nums) - 1
            b = nums[mid]

            while start < mid < end:
                a, c = nums[start], nums[end]
                sum = a + b + c

                if sum == 0:
                    if (a, b, c) not in s:
                        results.append([a, b, c])
                        s.add((a, b, c))
                    start += 1
                elif sum < 0:
                    start += 1
                else:
                    end -= 1

        return results