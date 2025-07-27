class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print("bottom - > top",end=' ')
        print("Stack:", self.items)

if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.display()
    print("Popped item:", stack.pop())
    stack.display()
    print("Top item:", stack.peek())
    print("Is stack empty?", stack.is_empty())
    stack.pop()
    stack.pop()
    print("Is stack empty after popping all items?", stack.is_empty())