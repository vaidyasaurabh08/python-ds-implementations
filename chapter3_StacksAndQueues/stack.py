"""
we can implement a stack in python using multiple data structures like:
1. Linked Lists
2. Python in built Lists (implemented as arrays in cpython)
3. collections.deque

I will implement using a collections.deque as that is the most straight forward approach and 
at the same time we are able to get optimized time complexities for all stack operations 

1. pop():      O(1):  remove the top item from the stack 
2. push(item):     O(1):  add an item tothe top of tehh stack 
3. peek():     O(1):  return the item at the top of the stack 
4. isEmpty():  O(1):  return True is the stack is empty
"""


class Stack:
    def __init__(self, values=None):
        if not values:
            self.stack = list()
        else:
            self.stack = list(values)

    def __str__(self):
        return str(self.stack)

    def push(self, item=None):
        if item:
            self.stack.append(item)
            return 0

    def pop(self):
        if not self.stack:
            return -1
        return self.stack.pop()

    def peek(self):
        if not self.stack:
            return -1
        else:
            return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0


if __name__ == "__main__":
    stc = Stack()
    print(stc)
    print(stc.isEmpty())
    stc.push(1)
    print(stc)
    stc.push(2)
    print(stc.isEmpty())
    print(stc)
    stc.pop()
    print(stc)
    stc.pop()
    print(stc)

    stc.pop()
    print(stc)
    print(stc.isEmpty())
