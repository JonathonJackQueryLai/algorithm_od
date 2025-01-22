# coding:utf -8

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    res = ListNode(None)
    node = res
    while list1 and list2:
        if list1.val <= list2.val:
            node.next = list1
            list1 = list1.next
        else:
            node.next = list2
            list2 = list2.next
        node = node.next
    while list1:
        node.next = list1
        list1 = list1.next
        node = node.next
    while list2:
        node.next = list2
        list2 = list2.next
        node = node.next
    return res.next


if __name__ == '__main__':
    li1 = ListNode(-9)
    li1.next = ListNode(3)
    li2 = ListNode(5)
    li2.next = ListNode(7)
    print(mergeTwoLists(li1, li2))
