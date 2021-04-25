 """
we can implement a queue in python using multiple data structures like:
1. Doubly Linked Lists
2. Python in built collections.deque (implemented as doubly linked list in cpython)


I will implement using collections.deque

1. remove():   O(1):  remove the first item from the list
2. add(item):  O(1):  add an item to end of the list
3. peek():     O(1):  return the item at the top of the list 
4. isEmpty():  O(1):  return True is the queue is empty
"""


from collections import deque

class Queue:
    def __init__(self, values=None):
        if not values:
            self.queue = deque()
        else:
            self.queue = deque(values)

    def __str__(self):
        return f"{self.queue}"

    def add(self, item=None):
        if not item:
            return -1
        self.queue.appendleft(item)

    def remove(self):
        if not self.queue:
            return -1
        return self.queue.pop()

    def peek(self):
        if not self.queue:
            return -1
        else:
            return self.queue[0]

    def isEmpty(self):
        return len(self.queue) == 0

if __name__ == "__main__":
    q = Queue()
    print(q)
    print(q.isEmpty())
    q.add(1)
    print(q)
    q.add(2)
    print(q.isEmpty())
    print(q)
    q.remove()
    print(q)
    q.remove()
    print(q)

    q.remove()
    print(q)
    print(q.isEmpty())

