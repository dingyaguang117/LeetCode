from collections import deque
from itertools import izip

class Solution(object):
	def search_deeper(self, beginWords, wordList, visited):
		ans = set()
		for word in beginWords:
			for i in xrange(len(word)):
				for char in self.chars:
					_word = word[:i] + char + word[i+1:] 
					if _word not in visited and _word in wordList:
						ans.add(_word)
		return ans

	def ladderLength(self, beginWord, endWord, wordList):
		"""
		:type beginWord: str
		:type endWord: str
		:type wordList: Set[str]
		:rtype: int
		"""

		if beginWord == endWord:
			return 1

		self.chars = 'abcdefghijklmnopqrstuvwxyz'
		
		words1, words2 = set([beginWord]), set([endWord])
		visited1, visited2 = words1, words2

		depth1, depth2 = 1, 1
		while True:
			words1 = self.search_deeper(words1, wordList, visited1)
			depth1 += 1
			if words1 & words2:
				return depth1 + depth2 -1
			visited1 |= words1

			words2 = self.search_deeper(words2, wordList, visited2)
			depth2 += 1
			if words1 & words2:
				return depth1 + depth2 -1
			visited2 |= words2

			if not words1 and not words2:
				return 0


if __name__ == '__main__':
	s = Solution()
	assert s.ladderLength('hit', 'cog', ["hot","dot","dog","lot","log"]) == 5
	assert s.ladderLength('hit', 'hot', ["hot"]) == 2
	assert s.ladderLength('hit', 'hit', ["hot"]) == 1
	assert s.ladderLength('hot', 'dog', ["hot", "dog"]) == 0