# For ease of implementation, we will create two classes, viz. SLinkedList and Node

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        listText = ""
        current = self.head
        while current:
            listText += current.data + "-"
            current = current.next
        print(listText, "\n")


    def insertAtStart(self, data):
        # if head is None, then head points to the new node 
        # if head is not None, then head points to the new node and new node next points to where head was pointing
        newNode = Node(data=data)
        
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def insertBetween(self, previousNodeData, data):
        # check if previousNode has a valid next pointer

        # create a new node 
        # find previous Node based on previousNodeData
        # point new node's next to where previous nodes next was pointing
        # point previous node's next to new node
        

        previousNode = None
        current = self.head
        while current:
            if current.data == previousNodeData:
                previousNode = current
            current = current.next
        
        if not previousNode:
            raise Exception("No node found with data = ", previousNodeData)


        newNode = Node(data=data)
        newNode.next = previousNode.next
        previousNode.next = newNode 

    def appendAtEnd(self, data):
        newNode = Node(data=data)
        current = self.head
        
        while(current.next):
            current = current.next
        current.next = newNode

    
    def deleteFirstNode(self):
        if not self.head:
            raise Exception("Linked List is empty")

        self.head = self.head.next


    def deleteLastNode(self):
        if not self.head:
            raise Exception("Linked List is empty")

        lastButOneNode = None
        current = self.head
        while(current.next):
            lastButOneNode = current
            current = current.next

        if lastButOneNode:
            lastButOneNode.next = None
        else:
            self.head = None


    def deleteNode(self, nodeData):
        if not self.head:
            raise Exception("List is empty")
        
        # 1. Find the node to delete
        # 2. Keep a track of the previous to current node
        # 3. Point prev node's next to the next of nodeToDelete


        # spl case where the node to delete is the head
        if(self.head.data == nodeData):
            self.head = self.head.next
            return

        previousNode = self.head
        current = self.head.next
        while(current.next):
            if (current.data == nodeData):
                previousNode.next = current.next
                return
            else:
                previousNode = current
                current = current.next
        
        # spl case where the node to delete is the last node
        if current.data == nodeData:
            previousNode.next = current.next
            return


sLinkedList = SLinkedList()


print("Inserting First at the start")
sLinkedList.insertAtStart("First")
sLinkedList.print()

print("Deleting Last node")
sLinkedList.deleteLastNode()
sLinkedList.print()

print("Inserting Second at the start")
sLinkedList.insertAtStart("Second")
sLinkedList.print()

print("Inserting Third at the start")
sLinkedList.insertAtStart("Third")
sLinkedList.print()

print("Appending end at the end")
sLinkedList.appendAtEnd("end")
sLinkedList.print()

print("Appending end2 at the end")
sLinkedList.appendAtEnd("end2")
sLinkedList.print()

print("Inserting end1 after end")
sLinkedList.insertBetween("end", "end1")
sLinkedList.print()

print("Deleting First node")
sLinkedList.deleteFirstNode()
sLinkedList.print()

print("Deleting Last node")
sLinkedList.deleteLastNode()
sLinkedList.print()

sLinkedList.print()
sLinkedList.deleteNode("end1")
sLinkedList.print()
