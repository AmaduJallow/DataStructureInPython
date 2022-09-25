class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self._first = None
        self._size = 0

    # !Node end here/////

    def push(self, data):
        if self._isempty():
            self._first = self.Node(data)
        else:
            node = self.Node(data)
            node.next = self._first
            self._first = node
        self._size += 1

    def _isempty(self):
        return self._size == 0

    def delete_head(self):
        if self._isempty():
            return
        elif self._size == 1:
            self._first = None
            self._first.next = None
            self._size = 0
        else:
            self._first = self._first.next
            self._size -= 1

    def display(self):
        current = self._first
        while current is not None:
            print(f"Current:{current.data}")
            current = current.next

    def size(self):
        return self._size


user = LinkedList()
user.push(12)
user.push(23)
user.push(24)
user.push(30)
user.push(44)
user.push(363)
user.push(360)
user.delete_head()
user.delete_head()
user.display()
print(user.size())
