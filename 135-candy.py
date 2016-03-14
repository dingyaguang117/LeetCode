class Node(object):
	def __init__(self, rank, value):
		self.rank = rank
		self.value = value

class Solution(object):



	def calc_order(self):

		self.rating_nodes = []

		for i, item in enumerate(self. ratings):
			self.rating_nodes.append(Node(i, item))
		self.rating_nodes.sort(key=lambda node: node.value)

	def max_neighbor(self, rank):
		ans = 0
		if rank != 0 and self.ratings[rank-1] < self.ratings[rank]:
			ans = self.gives[rank-1]
		if rank != len(self.ratings)-1 and self.ratings[rank+1] < self.ratings[rank]:
			ans = max(ans, self.gives[rank+1])
		return ans


	def candy(self, ratings):
		self.ratings = ratings
		self.gives = [0]*len(ratings)
		self.calc_order()

		for node in self.rating_nodes:
			print node.rank, node.value
			self.gives[node.rank] = self.max_neighbor(node.rank) + 1

		print self.gives
		return sum(self.gives)


if __name__ == '__main__':
	s = Solution()

	x = [1,2,3,4,5,6]
	assert s.candy(x) == 21

