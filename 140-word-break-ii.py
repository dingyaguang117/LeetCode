class Node(object):
	def __init__(self, end=False):
		self.next = [None] * 26
		self.word = None

	def add_next(self, edge, node):
		self.next[ord(edge)-ord('a')] = node

class TrieTree(object):
	def __init__(self):
		self.root = Node()

	def add_word(self, word):
		p = self.root
		for c in word:
			node = p.next[ord(c)-ord('a')]
			if node is None:
				node = Node()
				p.next[ord(c)-ord('a')] = node
			p = node
		p.word = word

	@classmethod
	def buildFromWords(cls, words):
		tree = cls()
		for word in words:
			tree.add_word(word)
		return tree

class Solution(object):

	def search(self, node, pos):
		c = self.s[pos]
		next = node.next[ord(c)-ord('a')]
		if next:
			if next.word:
				result_backup = self.result[:]
				self.result.append(next.word)
				# print 'append', pos, next.word
				if pos == self.len-1:
					self.results.append(' '.join(self.result))
					self.result = []
					return
				self.search(self.tree.root, pos+1)
				# print 'backup', result_backup, self.result
				self.result = result_backup
			
			if pos == self.len -1:
				return
			self.search(next, pos+1)
		else:
			return

	def wordBreak(self, s, wordDict):
		"""
		:type s: str
		:type wordDict: Set[str] 
		:rtype: List[str]
		"""
		self.result = []
		self.results = []
		self.s = s
		self.len = len(s)
		self.tree = TrieTree.buildFromWords(wordDict)
		self.search(self.tree.root, 0)
		# self.results.sort(reverse=True)
		return self.results

if __name__ == '__main__':
	s = Solution()
	print s.wordBreak('catsanddog', ["cat", "cats", "and", "sand", "dog"])
	print s.wordBreak('aabb', ['a', 'ab', 'b'])
	print s.wordBreak('bb', ["a","b","bbb","bbbb"])
	