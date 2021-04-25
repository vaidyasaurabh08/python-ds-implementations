# implement a stack with push pop and min functions, all  operations 
# should be O(1)

class Stack:
    def __init__(self):
        self.stack = []
        self.minStack = []
        self.currentMin = None

    def __str__(self):
        return f"{self.stack}, Min stack is {self.minStack}, Min is {self.currentMin}"

    def push(self, item):
        if not item:
            return -1

        self.stack.append(item)
        if not self.minStack:
            self.minStack.append(item)
        else:
            self.currentMin = self.minStack[-1]
            if item <= self.currentMin:
                self.minStack.append(item)
        
    def pop(self):
        poppedItem = self.stack.pop()
        if poppedItem == self.currentMin:
            self.minStack.pop()
            self.currentMin = self.minStack[-1]
            
    def min(self):
        if not self.currentMin:
            return -1
        return self.currentMin


if __name__ == "__main__":
    stack = Stack()
    stack.push(4)
    stack.push(10)
    stack.push(1)
    stack.push(1)
    stack.push(4)
    stack.push(0)

    print(stack)

    stack.pop()
    print(stack)

    stack.pop()
    print(stack)
    
    stack.pop()
    print(stack)
    
    stack.pop()
    print(stack)

