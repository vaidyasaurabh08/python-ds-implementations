import time, random
from LinkedLists.singlyLinkedList import SLinkedList


def remove_dups(ll: SLinkedList):
    '''
        O(N) as we would need to traverse the entire LL once
    '''

    if not ll.head:
        return
    
    seenVals = set()
    
    previous = None
    current = ll.head

    while(current):
        if current.data in seenVals:
            previous.next = current.next
        else:
            seenVals.add(current.data)
            previous = current
        
        current = current.next


def remove_dups_no_buffer(ll: SLinkedList):
    '''
        Two pointers
    '''
    current = ll.head
    
    while current:
        previousToRunner = current
        runner = current.next
        while runner:
            if current.data == runner.data:
                # remove runner from the Linked List
                #   1. point runner's previous node's next to runner's next
                previousToRunner.next = runner.next
            else:
                previousToRunner = runner

            runner = runner.next
        current = current.next

randomlist = random.sample(range(1, 10000), 1000)

test_cases = (
    ([], []),
    ([1,1,1,1], [1]),
    ([1,2,3,4,1,2,3,4], [1,2,3,4]),
    ([1,2,3], [1,2,3]),
)



def test_remove_dups():    
    for t_case in test_cases:
        values = t_case[0]
        expected = t_case[1]

        sLinkedList = SLinkedList()
        sLinkedList.addMultiple(values=values)
        remove_dups(sLinkedList)
        a = sLinkedList.get_values()
        b = expected
        print(a, "\n")
        print(b)
        assert sLinkedList.get_values() == expected


def test_remove_dups_no_buffer():
    for t_case in test_cases:
        values = t_case[0]
        expected = t_case[1]

        sLinkedList = SLinkedList()
        sLinkedList.addMultiple(values=values)
        remove_dups_no_buffer(sLinkedList)
        assert sLinkedList.get_values() == expected
    



if __name__ == '__main__':
    start = time.perf_counter()
    test_remove_dups()
    duration = time.perf_counter() - start
    print(f"Remove dups took {duration*1000} ms")

    start = time.perf_counter()
    test_remove_dups_no_buffer()
    duration = time.perf_counter() - start
    print(f"Remove dups no buffer took {duration*1000} ms")

