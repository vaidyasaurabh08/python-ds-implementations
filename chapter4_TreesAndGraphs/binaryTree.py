# Implementation of a Binary Tree where a node has at most 2 child nodes
# and for any given node the left node is smaller than itself and the 
# right node is greater than itself
# i.e. all left descendents <= n <= all right descendents

class Node:
    def __init__(self, data=None):
        if not data:
            raise Exception("Please provide data to construct a new node")
        
        self.data = data
        self.leftNode = None
        self.rightNode = None
        
    def insert(self, data):
        if not data:
            return
        
        if not self.data:
            self.data = data
            return
        
        if data < self.data:
            if not self.leftNode:
                self.leftNode = Node(data)
            else:
                self.leftNode.insert(data)
        
        elif data > self.data:
            if not self.rightNode:
                self.rightNode = Node(data)
            else:
                self.rightNode.insert(data)

        
    def printInOrder(self):
        # In order 
        if self.leftNode:
            self.leftNode.printInOrder()
        
        print(f" {self.data} ->", end="")

        if self.rightNode:
            self.rightNode.printInOrder()

    
    def printPreOrder(self):
        
        print(f" {self.data} ->", end="")

        if self.leftNode:
            self.leftNode.printPreOrder()

        if self.rightNode:
            self.rightNode.printPreOrder()


    def printPostOrder(self):
        if self.leftNode:
            self.leftNode.printPostOrder()

        if self.rightNode:
            self.rightNode.printPostOrder()

        print(f" {self.data} ->", end="")


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)

root.printInOrder()
print("\n")
root.printPreOrder()

print("\n")
root.printPostOrder()