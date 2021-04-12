import time, random
from LinkedLists.singlyLinkedList import SLinkedList


def find_kth_to_last_iterative(k: int, ll: SLinkedList):
    current = runner = ll.head
    
    for _ in range(k+1):
        try:
            runner = runner.next
        except AttributeError:
            print("k is greater than the length of the LL")
            return None
    
    while runner:
        runner = runner.next
        current = current.next
    
    return current.data


test_cases = (
    ([1,2,3,4,5,6,7,8], 3, 5),
    ([10,12,33,44], 3, 10),
    ([10,12,33,44], 1, 33),
    ([10,12,33,44], 0, 44),
)


def test_find_kth_to_last_iterative():
    for t_case in test_cases:
        values = t_case[0]
        k = t_case[1]
        expected = t_case[2]

        sLinkedList = SLinkedList()
        sLinkedList.addMultiple(values=values)
        
        assert find_kth_to_last_iterative(k=k, ll=sLinkedList) == expected

 
if __name__ == '__main__':
    test_find_kth_to_last_iterative()