# sort a given stack using a temp stack

from stack import Stack


def sortStack(stack: Stack):
    tempStack = Stack()

    tempItem = None
    count = 0

    while not stack.isEmpty():
        poppedItem = stack.pop()
        
        if tempStack.isEmpty():
            tempStack.push(poppedItem)
            continue
        
        while not tempStack.isEmpty() and poppedItem < tempStack.peek():
            stack.push(tempStack.pop())
        
        tempStack.push(poppedItem)

    return tempStack

if __name__ == '__main__':
    s = Stack()
    s.push(6); s.push(3), s.push(11), s.push(10); s.push(17), s.push(5)
    print(s)

    sorted_s = sortStack(s)
    print(sorted_s)

# python ./p5_sort_stack.py
# [6, 3, 11, 10, 17, 5]
# [3, 5, 6, 10, 11, 17]

