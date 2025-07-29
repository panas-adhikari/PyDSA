class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def insert(self,root,data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self.insert(root.left,data)
        elif data > root.data:
            root.right = self.insert(root.right,data)
        return root
    def search(self,root,data):
        if root is None:
            print("Data not found")
            return
        if data< root.data:
            self.search(root.left,data)
        elif data>root.data:
            self.search(root.right,data)
        if data == root.data:
            print("Data found")
    
def sample_use():    
    root = None 
    lista = [1,4,2,89,45,65,32,70,23,34,56,78,123,321,4556,654,567,765]
    mytree = BinarySearchTree()
    root = None
    for i in lista:
        root = mytree.insert(root , i)
    mytree.search(root,567)

if __name__ == '__main__':
    sample_use()