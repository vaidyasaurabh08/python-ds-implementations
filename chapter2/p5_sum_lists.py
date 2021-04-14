from LinkedLists.singlyLinkedList import SLinkedList





def sumLists(a_ll, b_ll, ll, carry=0):
    if a_ll and b_ll:
        sum_el = a_ll.data + b_ll.data + carry
        summ = sum_el%10
        remainder = sum_el//10
        ll.appendAtEnd(summ)
        return sumLists(a_ll.next, b_ll.next, ll, carry=remainder)
    elif a_ll and not b_ll:
        sum_el = a_ll.data + carry
        summ = sum_el%10
        remainder = sum_el//10
        ll.appendAtEnd(summ)
        return sumLists(a_ll.next, None, ll, carry=remainder)
    elif not a_ll and b_ll:
        sum_el = b_ll.data + carry
        summ = sum_el%10
        remainder = sum_el//10
        ll.appendAtEnd(summ)
        return sumLists(None, b_ll.next, ll, carry=remainder)
    else:
        ll.appendAtEnd(carry)
        return ll



test_cases = (
    ([2,9,5,6], [7,1,6], [9,0,2,7,0]),
    ([], [], [])
)

def test_add_lists():
    for t_case in test_cases:
        a_values = t_case[0]
        b_values = t_case[1]
        expected = t_case[2]


        a_ll = SLinkedList()
        a_ll.addMultiple(values=a_values)

        b_ll = SLinkedList()
        b_ll.addMultiple(values=b_values)

        result_ll = sumLists(a_ll.head, b_ll.head, SLinkedList())

        assert result_ll.get_values() == expected



        



if __name__ == '__main__':
    # a_ll = SLinkedList()
    # a_ll.addMultiple(values=[2,9,5,6])
    
    # b_ll = SLinkedList()
    # b_ll.addMultiple(values=[7,1,6])

    # a_ll.print()
    # b_ll.print()

    # result_ll = SLinkedList()

    # print(sumLists(a_ll.head, b_ll.head, result_ll))
    # result_ll.print()
    test_add_lists()


