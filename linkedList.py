class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def plug(self,node,data):
        if node is None:
            return Node(data)
        node.next = self.plug(node.next,data)
        return node
    def match(self , node , data):
        if node == None:
            print("Data not found")
            return 
        if node.data != data:
            return self.match(node.next , data)
        elif node.data == data:
            print("Data found")
            return
    def traverse(self,node):
        if node is None:
            return
        print(node.data)
        return self.traverse(node.next)
    def delete(self,node,data):
        if node is None:
            print("Deletion Data not found")
            return
        if node.data == data:
            return node.next
        current = node
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return node
            current = current.next
        return node


if __name__ == '__main__':
    myl = LinkedList()
    node = None
    for i  in range(10):
        node = myl.plug(node,i)
    myl.match(node , 8)
    myl.traverse(node)
    print()
    myl.delete(node,7)
    print()
    myl.traverse(node)