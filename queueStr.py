class HeadfixQueue:
    def __init__(self):
        self.items = []
        self.head = 0
        self.tail = 0
    
    def is_empty(self):
        return self.head == self.tail
    def enqueue(self, item):
        self.items.append(item)
        self.tail+=1
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from a empty queue")
        item = self.items[self.head]
        for i in range(len(self.items)-1):
            self.items[i] = self.items[i+1]
        self.items.pop()  # removing the last items after shifting
        self.tail -= 1
        return item
    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue items:", self.items[self.head:self.tail])
    def size(self):
        return self.tail - self.head


if __name__ == "__main__":
    myqueue = HeadfixQueue()
    myqueue.enqueue(1)
    myqueue.enqueue(2)
    myqueue.display()
    print(myqueue.size())
    print("Dequeue : ",myqueue.dequeue())
    myqueue.display()
    print(myqueue.size())