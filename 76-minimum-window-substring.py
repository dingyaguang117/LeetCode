import sys
from collections import defaultdict, deque

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        target = defaultdict(int)
        current = defaultdict(int)
        target_count = len(t)
        current_count = 0
        queue = deque()

        best = sys.maxint
        ans = ''

        for c in t:
            target[c] += 1

        for i, c in enumerate(s):
            if c not in target:
                continue

            if current[c] < target[c]:
                current_count += 1
            
            current[c] += 1
            queue.append(i)

            while queue:
                char = s[queue[0]]
                if current[char] > target[char]:
                    queue.popleft()
                    current[char] -= 1
                else:
                    break

            if current_count == target_count:
                # print queue
                if queue[-1] - queue[0] < best:
                    best = queue[-1] - queue[0]
                    ans = s[queue[0]: queue[-1]+1]
        return ans

if __name__ == '__main__':
    s = Solution()
    assert s.minWindow('ADOBECODEBANC', 'ABC') == 'BANC'
    assert s.minWindow('aa', 'aa') == 'aa'
    assert s.minWindow('aa', 'a') == 'a'