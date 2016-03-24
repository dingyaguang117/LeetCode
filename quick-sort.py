def swap(L, a, b):
	temp = L[a]
	L[a] = L[b]
	L[b] = temp


def quick_sort(L, begin, end):
	if begin >= end:
		return
	value = L[begin]
	plower = begin

	for p in xrange(begin+1, end+1):
		if L[p] < value:
			plower += 1
			swap(L, plower, p)
	swap(L, begin, plower)
	quick_sort(L, begin, plower-1)
	quick_sort(L, plower+1, end)



if __name__ == '__main__':
	L = [5,2,1,4,3,4,43,23,4,35,45,6,75,56,45,54,45 ,4566 ,45,6,58, 788]
	quick_sort(L, 0, len(L)-1)
	print L