from LinkedLists.singlyLinkedList import SLinkedList, Node


def remove_node(node:Node, ll:SLinkedList):
    '''
    As we just have access to the Node to be deleted, we copy over the 
    next node to the current node and delete the next node
    '''
    node.data = node.next.data
    node.next = node.next.next


sLinkedList = SLinkedList()
sLinkedList.addMultiple(values = [2,3,4,5,3,4,5,6,7])

print(sLinkedList.print())

nodeToDelete = sLinkedList.getNodeWithValue(7)
remove_node(node=nodeToDelete, ll=sLinkedList)

print(sLinkedList.print())