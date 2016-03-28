class Node(object):
    def __init__(self, key, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class DoublyLinkedList(object):
    def __init__(self, capacity):
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.size = 0

    def move_to_head(self, node):
        if self.head == node:
            return

        node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        self.head.prev = node
        node.prev = None
        node.next = self.head
        self.head = node


    def insert(self, key, val):
        deleted = None
        node = Node(key, val)
        if self.head == None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

        if self.size == self.capacity:
            deleted = self.tail
            self.tail.prev.next = None
            self.tail = self.tail.prev
        else:
            self.size += 1
        return node, deleted

    def show(self, reverse=False):
        print '-- show --'
        if reverse:
            p = self.tail
            while p:
                print p.key, p.val
                p = p.prev
        else:
            p = self.head
            while p:
                print p.key, p.val
                p = p.next
        print '-- end --'

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.list = DoublyLinkedList(capacity)
        self.map = {}
        self.capacity = capacity
        

    def get(self, key):
        """
        :rtype: int
        """
        node = self.map.get(key)
        if not node:
            return -1
        self.list.move_to_head(node)
        return node.val
        

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        node = self.map.get(key)
        if not node:
            node, deleted = self.list.insert(key, value)
            self.map[key] = node
            if deleted:
                del self.map[deleted.key]
        else:
            node.val = value
            self.list.move_to_head(node)


if __name__ == '__main__':
    l = LRUCache(2)
    l.set(2, 1)
    l.set(1, 1)
    # l.list.show()
    # l.list.show(True)
    print l.get(2)
    # l.list.show()
    # l.list.show(True)
    l.set(4, 1)
    # l.list.show()
    print l.get(1)
    print(l.get(2))
