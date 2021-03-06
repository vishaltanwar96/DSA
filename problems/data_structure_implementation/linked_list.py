class Node:

    def __init__(self, data, next_node=None):

        self.data = data
        self.next_node = next_node

    def __repr__(self):

        return '<Node %s>' % self.data


class LinkedList:

    def __init__(self, head):

        self.head = head
        self._count = 1

    def prepend(self, data):

        node = Node(data)
        current_head = self.head
        self.head = node
        self.head.next_node = current_head
        self._count += 1

    def pop(self):

        to_pop = self.head
        if to_pop is None:
            raise IndexError('Cannot pop from empty LinkedList')
        self.head = to_pop.next_node
        self._count -= 1
        return to_pop

    def __len__(self):

        return self._count

    def __reversed__(self):

        previous_node = None
        current = self.head
        while current:
            next_node = current.next_node
            current.next_node = previous_node
            previous_node = current
            current = next_node
        self.head = previous_node

    def __repr__(self):

        representation = []
        current = self.head
        while current:
            if current is self.head:
                representation.append('[Head %s]' % current.data)
            elif current.next_node is None:
                representation.append('[Tail %s]' % current.data)
            else:
                representation.append('[%s]' % current.data)
            current = current.next_node
        return ' -> '.join(representation)
