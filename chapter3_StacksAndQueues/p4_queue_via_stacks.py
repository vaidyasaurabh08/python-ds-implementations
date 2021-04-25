# Implement a Queue using 2 stacks
from stack import Stack
import copy

class MyQueue:
    def __init__(self):
        self.stackNew = Stack()
        self.stackOld = Stack()


    def add(self, item):
        if not item:
            return -1
        
        if self.stackOld.isEmpty():
            return self.stackNew.push(item)
            
        
        self.reverseStacks(self.stackOld, self.stackNew)
        self.stackOld = Stack()
        self.stackNew.push(item)

    
    def remove(self):
        if self.stackNew.isEmpty():
            return self.stackOld.pop()
            
        
        self.reverseStacks(self.stackNew, self.stackOld)
        self.stackNew = Stack()
        return self.stackOld.pop()

    
    def reverseStacks(self, stack1, stack2):
        while not stack1.isEmpty():
            stack2.push(stack1.pop())

    
    def __str__(self):
        if self.stackOld.isEmpty() and self.stackNew.isEmpty():
            q = []
        elif self.stackOld.isEmpty():
            temp = copy.deepcopy(self.stackNew.stack)
            temp.reverse()
            q = temp
        elif self.stackNew.isEmpty():
            temp = copy.deepcopy(self.stackOld.stack)
            temp.reverse()
            q = temp
        return f"Stack Old is {self.stackOld} and Stack New is {self.stackNew} and Q is {q}"

        

if __name__ == '__main__':
    q = MyQueue()
    q.add(1)
    print(q)

    q.add(2)
    print(q)

    q.add(3)
    print(q)

    q.remove()
    print(q)

    q.remove()
    print(q)

    q.remove()
    print(q)

