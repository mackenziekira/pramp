class Stack(object):

    # initialize an empty list
    def __init__(self):
        self.items = []

    # push a new item to the last index
    def push(self, item):
        self.items.append(item)

    # remove the last item
    def pop(self):
        # if the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None
        return self.items.pop()

    # see what the last item is
    def peek(self):
        if not self.items:
            return None
        return self.items[-1]


class MaxStack(Stack):

    def __init__(self):
        super(MaxStack, self).__init__()
        self.max_stack = Stack()

    def push(self, item):
        self.items.append(item)
        if not self.max_stack.peek() or item >= self.max_stack.peek():
            self.max_stack.push(item)

    def pop(self):
        if not self.items:
            return None
        if self.items[-1] == self.max_stack.peek():
            self.max_stack.pop()
        return self.items.pop()

    def get_max(self):
        """get max num from a stack

        >>> a = MaxStack()
        >>> a.push(5)
        >>> a.push(9)
        >>> a.push(11)
        >>> a.push(1)
        >>> print a.get_max()
        11

        >>> a = MaxStack()
        >>> print a.get_max()
        None
        """
        return self.max_stack.peek()

if __name__ == "__main__":
    import doctest
    doctest.testmod()



